import asyncio
import random

from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from django.core.mail import send_mail

from users.models import CustomUser, UserAssets
from users.serializers import UserSerializer, validate_email

@throttle_classes([AnonRateThrottle])
class VerifyCodeView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        """
        获取验证码，验证码有效期120秒
        参数：
        {
            email: 邮箱
        }
        :param request:
        :return:
        """
        email = request.data.get('email', '')
        if validate_email(email):
            verify_code = cache.get(email)
            if verify_code:
                return Response(data={"message": "验证码发送成功"}, status=status.HTTP_200_OK)
            try:
                six_digit_number = str(random.randint(100000, 999999))
                cache.set(email, six_digit_number, 2 * 60) # 2分钟有效期
                # 使用事件循环运行异步函数
                send_mail(subject="AI大师工具箱验证码",
                          message=f"您的验证码是{six_digit_number}, 有效期120秒",
                          from_email= settings.DEFAULT_FROM_EMAIL,
                            recipient_list= [email])
                return Response(data={"message": "验证码发送成功"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={"error": "验证码发送失败"}, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(data={'error': '邮箱格式错误'}, status=status.HTTP_400_BAD_REQUEST)


@throttle_classes([AnonRateThrottle])
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email', '')
        if not validate_email(email):
            return Response(data={'error': '账号输入错误'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.filter(email=email).first()
        if user:
            return Response(data={'error': '账号已经存在，请直接登录'}, status=status.HTTP_400_BAD_REQUEST)
        verify_code = str(request.data.pop('verify_code', 'x'))
        password = request.data.pop('password', '123456')
        if verify_code != cache.get(email):
            return Response(data={'error': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        s = UserSerializer(data = request.data, partial=True)
        if s.is_valid():
            s.save()
            s.instance.set_password(password)
            s.instance.save()
            # 创建用户时创建用户资产表
            invite_code = 0
            while True:
                new_value = random.randint(int(1e7+1), int(1e8-1))
                if not UserAssets.objects.filter(invite_code=new_value).exists():
                    invite_code = new_value
                    break
            UserAssets.objects.create(user=s.instance, invite_code=invite_code)
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
