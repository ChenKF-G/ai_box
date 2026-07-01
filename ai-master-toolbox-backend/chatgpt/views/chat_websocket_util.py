import json
from datetime import datetime

import requests
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from django.core.cache import cache
from chatgpt.models import ChatContent
from chatgpt.serializers import ChatContentOnlySerializer, ChatUsageSerializer
from chatgpt.views.chat_errors import ApiError, NoRightsError, OverHourThrottleError, OverDayThrottleError
from config import CHATGPT_CONFIG
from users.models import CustomUser, UserAssets
from utils.cache_util import ChatGPTCache

import logging
logger = logging.getLogger('ai_master_toolbox')

def get_user(token, user_id):
    if token and user_id:
        try:
            # 解码 JWT token
            access_token = AccessToken(token)
            token_user_id = access_token.payload.get('user_id')
            user = CustomUser.objects.get(id=token_user_id)
            if user and user.id == user_id:
                return user
        except Exception as e:
            return None
    return None

def create_chat_usage(user, usage):
    usage_serializer = ChatUsageSerializer(data=usage, partial=True)
    if usage_serializer.is_valid():
        usage_serializer.save(user=user)

def check_rights(user):
    # 检查免费使用次数是否超过
    key = ChatGPTCache.chat_day_left_free_count_key(user)
    count = cache.get(key)
    logger.debug(f'{key}: left count:{count}')
    if count is None:
        cache.set(key,
                  CHATGPT_CONFIG.FREE_COUNT_OF_CHATGPT_PER_DAY,
                  ChatGPTCache.chat_day_left_free_count_key_expired_time)
    count = cache.get(key)
    if count > 0:
        return True

    # 系统管理员可以免费使用
    if user.is_superuser:
        return True

    # 检查是否是付费用户，使用期限是否过期
    user_assets = UserAssets.objects.get(user=user)
    chatgpt_expired_time = user_assets.chatgpt_expired_time
    # 如果没有过期则返回true
    if chatgpt_expired_time < datetime.now():
        raise NoRightsError()

    return False

def check_throttle(user):
    # 检查用户是否超过了限流设置
    day_key = ChatGPTCache.chat_left_count_per_day_key(user)
    hour_key = ChatGPTCache.chat_left_count_per_hour_key(user)

    if cache.get(hour_key) is None:
        cache.set(hour_key,
                  CHATGPT_CONFIG.LIMIT_COUNT_OF_CHATGPT_PER_HOUR,
                  ChatGPTCache.chat_left_count_per_hour_key_expired_time)
    hour_left_count = cache.get(hour_key)

    if hour_left_count <= 0:
        raise OverHourThrottleError()

    if cache.get(day_key) is None:
        cache.set(day_key,
                  CHATGPT_CONFIG.LIMIT_COUNT_OF_CHATGPT_PER_DAY,
                  ChatGPTCache.chat_left_count_per_day_key_expired_time)

    if user.is_superuser:
        return True

    day_left_count = cache.get(day_key)
    if day_left_count <= 0:
        raise OverDayThrottleError()

    return True

def update_lefe_count(user):
    if user.is_superuser:
        return True

    # 更新免费使用次数是否超过
    chat_day_left_free_count_key = ChatGPTCache.chat_day_left_free_count_key(user)
    free_count = cache.get(chat_day_left_free_count_key)
    if free_count > 0:
        cache.set(chat_day_left_free_count_key,
                  free_count - 1,
                  ChatGPTCache.chat_day_left_free_count_key_expired_time)

    # 更新限流次数
    day_key = ChatGPTCache.chat_left_count_per_day_key(user)
    hour_key = ChatGPTCache.chat_left_count_per_hour_key(user)

    hour_left_count = cache.get(hour_key)
    if hour_left_count > 0:
        cache.set(hour_key, hour_left_count - 1, ChatGPTCache.chat_left_count_per_hour_key_expired_time)

    day_left_count = cache.get(day_key)
    if day_left_count > 0:
        cache.set(day_key, day_left_count - 1, ChatGPTCache.chat_left_count_per_day_key_expired_time)

def get_history_messages(conversation):
    query_set = ChatContent.objects.filter(conversation=conversation)
    chat_list_serializer = ChatContentOnlySerializer(instance=query_set, many=True)
    messages = chat_list_serializer.data

    # 截取massages的前5条后最后5条
    if len(messages) > 5:
        messages = messages[-5:]
    return messages


chat_api_url = settings.OPENAI_SERVER + '/api/openai/chat/'

def get_completion_from_openai(user, messages, stream=True):
    max_tokens = 1000
    if user.is_superuser:
        max_tokens = 2000

    response = requests.post(chat_api_url, data={
        'messages': json.dumps(messages),
        'max_tokens':max_tokens,
        'stream': True
    }, stream=True)

    if response.status_code != 200:
        raise ApiError()
    def data_gen():
        for line in response.iter_lines(decode_unicode=True):
            if not line.startswith('data: '):
                continue
            chunk = json.loads(line[len('data: '):])
            yield chunk

    return data_gen()

