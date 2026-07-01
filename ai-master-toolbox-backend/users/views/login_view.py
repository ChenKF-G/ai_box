from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser

@throttle_classes([AnonRateThrottle])
class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        # 从请求中获取用户名和密码
        username = request.data.get('username')
        password = request.data.get('password')

        user = CustomUser.objects.filter(username=username).first()

        if not user:
            user = CustomUser.objects.filter(email=username).first()

        if not user:
            user = CustomUser.objects.filter(phone=username).first()

        if not user:
            return Response({'error': '该用户不存在'}, status=status.HTTP_400_BAD_REQUEST)

        # 使用 Django 的认证系统来验证用户
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            if user.is_active:
                # 用户验证成功，生成 JWT 令牌
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # 登录用户
                login(request, user)

                # 返回令牌给客户端
                return Response({'token': access_token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': '该用户未激活'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
