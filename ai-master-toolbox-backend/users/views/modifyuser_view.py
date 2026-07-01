import random

from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers import validate_phone,validate_username

class ModifyUserView(APIView):
    def put(self, request):
        if 'phone' in request.data:
            email = request.data.get('email', '')  #邮箱
            verify_code = request.data.pop('verify_code', 'x')  #验证码
            new_phone = request.data.get('phone', '')  #手机号

            # 检查新手机号的有效性
            if not validate_phone(new_phone):
                return Response({'error': '手机号码输入错误'}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            # 检查新手机号是否已经被使用
            if CustomUser.objects.filter(phone=new_phone).exists():
                return Response({'error': '手机号已被使用'}, status=status.HTTP_400_BAD_REQUEST)
            # 验证码验证
            if verify_code != cache.get(email):
                return Response({'error': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

            # 更新用户手机号
            user.phone = new_phone
            user.save()

            return Response({'message': '手机号更换成功'}, status=status.HTTP_200_OK)
        if 'username' in request.data:
            user = request.user

            email = request.data.get('email', '')  # 邮箱
            verify_code = request.data.pop('verify_code', 'x')  # 验证码
            new_username = request.data.get('username', '')  # 用户名

            # 用户名是否符合规范
            if not validate_username(new_username):
                return Response({'error': '用户名不符合规范'}, status=status.HTTP_400_BAD_REQUEST)

            # 用户名是否唯一
            if CustomUser.objects.filter(username=new_username).exists():
                return Response({'error': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)

            # 验证码验证
            if verify_code != cache.get(email):
                return Response({'error': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

            user.username = new_username
            user.save()

            return Response({'message': '用户名更改成功'}, status=status.HTTP_200_OK)

class ModifyPasswordView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def put(self,request):
        email = request.data.get('email','') #邮箱
        verify_code = str(request.data.pop('verify_code', 'x'))
        password = request.data.get('password','')

        # 验证码验证
        if verify_code != cache.get(email):
            return Response({'error': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

        #用户名是否符合规范
        if not password or len(password) < 6:
            return Response({'error':'密码不符合规范'},status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'error': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(password)
        user.save()
        return Response({'message': '密码重置成功'},status=status.HTTP_200_OK)



