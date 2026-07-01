from channels.generic.websocket import WebsocketConsumer

from utils.utils import num_tokens_from_messages
from .chat_errors import ChatError, NoAuthError
from .chat_websocket_util import *
from ..models import Conversation
import logging
logger = logging.getLogger('ai_master_toolbox')

class EventType:
    auth = 'auth'
    send_message = 'send_message'
    send_received = 'send_received'
    response_message = 'response_message'
    response_finished = 'response_finished'
    re_generate = 're_generate'
    title_changed = 'title_changed'
    error = 'error'

class ChatWebSocket(WebsocketConsumer):
     def connect(self):
        logger.debug('连接成功')
        self.accept()

     def disconnect(self, close_code):
        logger.debug('连接关闭')
        pass

     def receive(self, text_data):
        """
        text_data 是字符串，但是符合json格式
        {
            eventType: # 事件类型
            content: # 内容
        }
        """
        data = json.loads(text_data)
        eventType = data['eventType']
        if eventType == EventType.auth:
            """
                发送权限内容格式
                {
                    eventType， user_id， token
                }
            """
            try:
                user_id = data['user_id']
                token = data['token']
                user =  get_user(token, user_id)
                if not user:
                     self.close()
                self.user = user
                self.send(text_data=json.dumps({
                    'eventType': EventType.auth,
                    'content': 'pass'
                }))
            except Exception as e:
                 self.send(json.dumps({
                    'eventType': EventType.error,
                    'content': str(e)
                }))
        if eventType == EventType.send_message or eventType == EventType.re_generate:
            """
                发送消息内容格式
                {
                    eventType， content， conversation_id
                }
            """
            try:
                if not self.user:
                    raise NoAuthError()
                check_rights(self.user)
                logger.debug(f'user:{self.user.id} has rights')
                check_throttle(self.user)
                logger.debug(f'user:{self.user.id} in throttle rules')

                conversation_id = data['conversation_id']
                conversation = Conversation.objects.get(id=conversation_id)

                if not (conversation and conversation.user.id == self.user.id):
                    raise Exception('会话不存在或者不属于该用户')

                self.conversation = conversation

                if eventType == EventType.send_message:
                    # 客户端发送消息过来
                    content = data['content']
                    if not content:
                        raise Exception('会话内容不能为空')

                    ChatContent.objects.create(conversation=conversation, content=content, role='user')
                else:
                    # 重新生成
                    # 获取最新的一条聊天记录
                    latest_chat_content = ChatContent.objects.\
                        filter(conversation=conversation).\
                        order_by('-timestamp').first()
                    if not latest_chat_content:
                        raise ChatError('该会话还没有聊天记录，无法重新生成')
                    if latest_chat_content.role != 'user':
                        # 如果不是用户发送的消息，那就先删除再重新生成
                        latest_chat_content.delete()

                update_lefe_count(self.user)
                messages =  get_history_messages(conversation)

                prompt_tokens =  num_tokens_from_messages(messages)
                self.usage = {
                    'prompt_tokens': prompt_tokens,
                    'completion_tokens': 0
                }
                self.response_total_messages = []

                completion = get_completion_from_openai(self.user, messages)
                logger.debug('start sending message')
                for chunk in completion:
                    choice = chunk['choices'][0]
                    delta = choice['delta']
                    if choice['finish_reason'] == 'stop':
                        logger.debug('sending message finished')
                        # 记录使用情况
                        create_chat_usage(self.user, self.usage)
                        self.usage = None
                        total_response = ''.join(self.response_total_messages)
                        if len(total_response) >= 4000:
                            total_response = total_response[:4000]
                        ChatContent.objects.create(
                            conversation=conversation,
                            content= total_response,
                            role='assistant')
                        self.response_total_messages = None
                        self.send(json.dumps({
                            'eventType': EventType.response_finished
                        }))
                        self.change_conversation_title(conversation)
                    else:
                        content = delta['content']
                        self.usage["completion_tokens"] +=  num_tokens_from_messages([{
                            'content': content
                        }])
                        self.response_total_messages.append(content)
                        self.send(json.dumps({
                            'eventType': EventType.response_message,
                            'content': content,
                            'conversation_id': conversation_id,
                            'role': 'assistant'
                        }))
            except Exception as e:
                try:
                    logger.debug('未知错误：' + str(e.args))
                    self.send(json.dumps({
                        'eventType': EventType.error,
                        'content': e.to_dict() if isinstance(e, ChatError) else str(e.args)
                    }))
                except Exception as e:
                    logger.debug('异常处理出错：' + str(e.args))
                    pass


     def change_conversation_title(self, conversation):
         try:
             if conversation.title != '无标题':
                 return
             messages = get_history_messages(conversation)
             messages.append({
                 'role': 'user',
                 'content': '请根据以上聊天信息，直接返回一个合理的对话标题，中文名字10个字以内，英文名字5个单词以内'
             })

             prompt_tokens = num_tokens_from_messages(messages)
             self.usage = {
                 'prompt_tokens': prompt_tokens,
                 'completion_tokens': 0
             }
             title_total_messages = []

             completion = get_completion_from_openai(self.user, messages)
             for chunk in completion:
                 choice = chunk['choices'][0]
                 delta = choice['delta']
                 if choice['finish_reason'] == 'stop':
                     # 记录使用情况
                     create_chat_usage(self.user, self.usage)
                     new_title = ''.join(title_total_messages)
                     if len(new_title) >= 10:
                         new_title = new_title[:10] + '...'
                     conversation.title = new_title
                     conversation.save()
                 else:
                     content = delta['content']
                     self.usage["completion_tokens"] += num_tokens_from_messages([{
                         'content': content
                     }])
                     title_total_messages.append(content)
                     self.send(json.dumps({
                         'eventType': EventType.title_changed,
                         'content': content,
                         'conversation_id': conversation.id,
                     }))
             pass
         except Exception as e:
             try:
                 logger.debug('未知错误：' + str(e.args))
                 self.send(json.dumps({
                     'eventType': EventType.error,
                     'content': e.to_dict() if isinstance(e, ChatError) else str(e.args)
                 }))
             except Exception as e:
                 logger.debug('异常处理出错：' + str(e.args))
                 pass


