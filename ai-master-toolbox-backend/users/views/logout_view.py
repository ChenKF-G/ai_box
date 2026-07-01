from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser

class ExitLoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        # 设置令牌失效
        try:
            logout(request)
            RefreshToken.for_user(request.user)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)