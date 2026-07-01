import json

from rest_framework.views import APIView
from django.utils import timezone

from api_log.models import APIAccessLog


class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.should_log_request(request):
            # 记录请求的开始时间
            request._api_access_start_time = timezone.now()

            request.cached_body = request.body

            response = self.get_response(request)

            # 计算请求处理时间
            request._api_access_end_time = timezone.now()
            request._api_access_processing_time = (
                request._api_access_end_time - request._api_access_start_time
            ).total_seconds() * 1000  # 毫秒为单位

            # 记录访问日志到数据库，包括API名称和请求参数
            self.log_api_access(request, response)

            return response
        else:
            # 如果不需要记录请求，直接继续处理请求
            return self.get_response(request)

    def log_api_access(self, request, response):
        # 获取请求信息
        method = request.method
        path = request.path
        status_code = response.status_code
        processing_time = request._api_access_processing_time

        # 获取API名称，如果视图类有设置名称的话
        api_name = self.get_api_name(request)

        # 获取请求参数
        parameters = json.dumps(self.get_request_params(request))

        # 获取响应数据
        response_data = '' if not hasattr(response, 'data') else response.data

        # 创建APIAccessLog对象并保存到数据库
        APIAccessLog.objects.create(
            user_id=request.user.id,
            api_name=api_name,
            method=method,
            path=path,
            parameters=parameters,
            status_code=status_code,
            response_data=response_data,
            processing_time=processing_time
        )

    def should_log_request(self, request):
        # get请求查询不做记录
        if request.method == 'GET':
            return False

        # api文档查询不做记录
        if 'doc' in request.path:
            return False

        return True

    def get_api_name(self, request):
        # 获取API名称，如果视图类有设置名称的话
        try:
            if hasattr(request.resolver_match.func, "view_class"):
                view_class = request.resolver_match.func.view_class
                if issubclass(view_class, APIView):
                    return view_class.__name__
        except:
            return "Unknown"
        return "Unknown"

    def get_request_params(self, request):
        # 获取请求参数
        if request.method == "GET":
            # 对于GET请求，将查询字符串参数记录下来
            return request.GET
        else:
            # 对于POST请求，将表单数据或JSON数据记录下来
            content_type = request.content_type
            if content_type == "application/x-www-form-urlencoded":
                # 表单数据
                return request.POST
            elif content_type == "application/json":
                # JSON数据
                try:
                    return json.loads(request.cached_body.decode('utf-8'))
                except Exception as e:
                    pass
        # 对于其他请求方法或无法解析的数据，返回空字典
        return {}

