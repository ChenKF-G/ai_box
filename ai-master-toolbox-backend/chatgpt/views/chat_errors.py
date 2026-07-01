import json
class ChatError(Exception):
    """自定义异常类的文档字符串（可选）"""

    def __init__(self, message, code=400):
        super().__init__(message)
        self.message = message
        self.code = 400

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message
        }

    def __str__(self):
        return json.dumps({
            'code': self.code,
            'message': self.message
        })

class NoAuthError(ChatError):
    def __init__(self):
        message = '用户没有登录'
        code = 401
        super().__init__(message, code)
        self.message = message
        self.code = code

class NoRightsError(ChatError):
    def __init__(self):
        message = '已经到达免费使用上限'
        code = 426
        super().__init__(message, code)
        self.message = message
        self.code = code

class OverHourThrottleError(ChatError):
    def __init__(self):
        message = '超过一小时内的使用上限，请休息片刻，稍后重试'
        code = 429
        super().__init__(message, code)
        self.message = message
        self.code = code

class OverDayThrottleError(ChatError):
    def __init__(self):
        message = '超过一天内的使用上限，请休息片刻，稍后重试'
        code = 429
        super().__init__(message, code)
        self.message = message
        self.code = code

class ApiError(ChatError):
    def __init__(self):
        message = '服务器或网络错误，请稍后刷新重试'
        code = 500
        super().__init__(message, code)
        self.message = message
        self.code = code
