from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser, UserAssets
from users.permissions import UserAssetsDetailViewPermission
from users.serializers import UserAssetsSerializer


class UserAssetsDetailView(APIView):
    permission_classes = [UserAssetsDetailViewPermission]  # 配置登录权限

    def get(self,request, pk):
        user = request.user if pk == 0 else CustomUser.objects.get(pk=pk)
        if not user:
            return Response(data={'error':'用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
        user_assets = UserAssets.objects.get(user=user)
        s = UserAssetsSerializer(instance=user_assets)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user if pk == 0 else CustomUser.objects.get(pk=pk)
        user_assets = UserAssets.objects.get(user=user)
        s = UserAssetsSerializer(instance=user_assets, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)