from rest_framework.throttling import SimpleRateThrottle

class ChatContentListThrottle(SimpleRateThrottle):
    # 定义不同用户类型的速率限制
    rate = '10/minute'
    def allow_request(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method == 'GET':
            # get方法不限流
            return True

        # 调用父类方法来进行速率限制检查
        return super().allow_request(request, view)

    def get_cache_key(self, request, view):
        return f'user:{request.user.id}:ChatContentListThrottle'

class ChatResponseThrottling(SimpleRateThrottle):
    # 定义不同用户类型的速率限制
    rate = '10/minute'

    def allow_request(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method == 'GET':
            # get方法不限流
            return True

        # 调用父类方法来进行速率限制检查
        return super().allow_request(request, view)

    def get_cache_key(self, request, view):
        return f'user:{request.user.id}:ChatResponseThrottling'