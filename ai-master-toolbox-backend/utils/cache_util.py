from datetime import date, datetime


class ChatGPTCache:
    # 对话列表缓存时间
    chat_content_list_expired_time = 1 * 60 * 60  # 1h

    # 每天的剩余免费使用次数缓存时间
    chat_day_left_free_count_key_expired_time = 24 * 60 * 60  # 24h = 1d

    # 每天剩余的使用次数缓存时间（不超过每天使用次数上限）
    chat_left_count_per_day_key_expired_time = 24 * 60 * 60  # 24h = 1d

    # 每小时剩余的使用次数缓存时间（不超过每小时使用次数上限）
    chat_left_count_per_hour_key_expired_time = 1 * 60 * 60  # 1h

    @staticmethod
    def chat_content_list_key(user, conversation_id):
        return f"chatcontent:{conversation_id}:"

    @staticmethod
    def chat_day_left_free_count_key(user):
        return f"user:{user.id}:chat_day_left_free_count_key:{str(date.today())}"

    @staticmethod
    def chat_left_count_per_hour_key(user):
        return f"user:{user.id}:chat_left_count_per_hour_key:{str(datetime.now().hour)}"

    @staticmethod
    def chat_left_count_per_day_key(user):
        return f"user:{user.id}:chat_left_count_per_day_key:{str(date.today())}"




