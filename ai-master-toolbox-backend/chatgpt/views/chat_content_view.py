from datetime import datetime
from django.core.cache import cache
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from chatgpt.chatgpt_throttling import ChatContentListThrottle, ChatResponseThrottling
from chatgpt.models import Conversation, ChatContent
from chatgpt.serializers import ChatContentOnlySerializer, \
    ChatContentDetailSerializer, ChatUsageSerializer
from config import CHATGPT_CONFIG
from users.models import UserAssets
from utils.cache_util import ChatGPTCache

class ChatContentListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ChatContentListThrottle]

    def get(self, request, pk):
        conversation = Conversation.objects.filter(pk=pk).first()
        if not conversation:
            return Response(data={'error': 'conversation不存在'},
                            status=status.HTTP_400_BAD_REQUEST)
        if conversation.user.id != request.user.id:
            return Response(data={'error': '该聊天不存在或者不属于当前用户'},
                            status=status.HTTP_400_BAD_REQUEST)
        query_set = ChatContent.objects.filter(conversation=conversation)
        s = ChatContentDetailSerializer(instance=query_set, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        conversation = Conversation.objects.filter(pk=pk).first()
        if conversation.user.id != request.user.id:
            return Response(data={'error': '该聊天不存在或者不属于当前用户'},
                            status=status.HTTP_400_BAD_REQUEST)
        s = ChatContentDetailSerializer(data=request.data, partial=True)
        if s.is_valid():
            s.save(conversation=conversation)
            s.instance.role = 'user' # 代表是用户发送的聊天记录内容
            s.instance.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatResponseBaseView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ChatResponseThrottling]

    def has_rights(self, request):
        # 检查免费使用次数是否超过
        key = ChatGPTCache.chat_day_left_free_count_key(request)
        count = cache.get(key)
        if count is None:
            cache.set(key,
                      CHATGPT_CONFIG.FREE_COUNT_OF_CHATGPT_PER_DAY,
                      ChatGPTCache.chat_day_left_free_count_key_expired_time)
        count = cache.get(key)
        if count > 0:
            return True

        user = request.user

        # 系统管理员可以免费使用
        if user.is_superuser:
            return True

        # 检查是否是付费用户，使用期限是否过期
        user_assets = UserAssets.objects.get(user=user)
        chatgpt_expired_time = user_assets.chatgpt_expired_time
        # 如果没有过期则返回true
        if chatgpt_expired_time > datetime.now():
            return True

        return False

    def check_throttle(self, request):
        # 检查用户是否超过了限流设置
        day_key = ChatGPTCache.chat_left_count_per_day_key(request)
        hour_key = ChatGPTCache.chat_left_count_per_hour_key(request)

        if cache.get(hour_key) is None:
            cache.set(hour_key,
                      CHATGPT_CONFIG.LIMIT_COUNT_OF_CHATGPT_PER_HOUR,
                      ChatGPTCache.chat_left_count_per_hour_key_expired_time)
        hour_left_count = cache.get(hour_key)

        if hour_left_count <= 0:
            return False

        if cache.get(day_key) is None:
            cache.set(day_key,
                      CHATGPT_CONFIG.LIMIT_COUNT_OF_CHATGPT_PER_DAY,
                      ChatGPTCache.chat_left_count_per_day_key_expired_time)

        day_left_count = cache.get(day_key)
        if day_left_count <= 0:
            return False

        return True

    def update_lefe_count(self, request):
        # 更新免费使用次数是否超过
        chat_day_left_free_count_key = ChatGPTCache.chat_day_left_free_count_key(request)
        free_count = cache.get(chat_day_left_free_count_key)
        if free_count > 0:
            cache.set(chat_day_left_free_count_key, free_count - 1)

        # 更新限流次数
        day_key = ChatGPTCache.chat_left_count_per_day_key(request)
        hour_key = ChatGPTCache.chat_left_count_per_hour_key(request)

        hour_left_count = cache.get(hour_key)
        if hour_left_count > 0:
            cache.set(hour_key, hour_left_count - 1)

        day_left_count = cache.get(day_key)
        if day_left_count > 0:
            cache.set(day_key, day_left_count - 1)

    def get_history_messages(self, conversation):
        query_set = ChatContent.objects.filter(conversation=conversation)
        chat_list_serializer = ChatContentOnlySerializer(instance=query_set, many=True)
        messages = chat_list_serializer.data

        # 截取massages的前5条后最后5条
        if len(messages) > 10:
            messages = messages[:5] + messages[-5:]
        return messages

    def get_completion_from_openai(self, messages, max_tokens):
        return None


class ChatResponseForAnswerView(ChatResponseBaseView):
    def post(self, request, pk):
        if not self.has_rights(request):
            return Response(data={'error': '已经到达免费使用上限'}, status=status.HTTP_426_UPGRADE_REQUIRED)

        if not self.check_throttle(request):
            return Response(
                data={'error': '使用频率过高，请休息片刻，稍后重试'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        conversation = Conversation.objects.filter(pk=pk).first()
        messages = self.get_history_messages(conversation)
        max_tokens = 2000 if request.user.is_superuser else 500
        try:
            completion = self.get_completion_from_openai(messages, max_tokens)
            # 记录使用情况
            usage_serializer = ChatUsageSerializer(data=completion.usage, partial=True)
            if usage_serializer.is_valid():
                usage_serializer.save(user=request.user)

            s = ChatContentDetailSerializer(data=completion.choices[0].message, partial=True)
            if s.is_valid():
                s.save(conversation=conversation)
                # 更新剩余使用次数
                self.update_lefe_count(request)
                return Response(data=s.data, status=status.HTTP_200_OK)
            else:
                return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)

class ChatResponseForTitleView(ChatResponseBaseView):
    def post(self, request, pk):
        if not self.has_rights(request):
            return Response(data={'error': '已经到达免费使用上限'}, status=status.HTTP_426_UPGRADE_REQUIRED)

        if not self.check_throttle(request):
            return Response(
                data={'error': '使用频率过高，请休息片刻，稍后重试'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        conversation = Conversation.objects.filter(pk=pk).first()
        if conversation.title != '无标题':
            return Response(data={'error': '该会话已经有标题'}, status=status.HTTP_400_BAD_REQUEST)
        messages = self.get_history_messages(conversation)
        messages.append({
            'role': 'user',
            'content': '请根据历史聊天信息，为这次对话取一个标题，中文名字10个字以内，英文名字5个单词以内'
        })
        max_tokens = 500
        try:
            completion = self.get_completion_from_openai(messages, max_tokens)
            # 记录使用情况
            usage_serializer = ChatUsageSerializer(data=completion.usage, partial=True)
            if usage_serializer.is_valid():
                usage_serializer.save(user=request.user)

            title = completion.choices[0].message.content
            if title:
                conversation.title = title
                conversation.save()
                # 更新剩余使用次数
                self.update_lefe_count(request)
                return Response(data={'title': title}, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': '生成标题失败,请重试'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)





