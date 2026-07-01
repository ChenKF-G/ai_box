from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from users.permissions import UserDetailViewPermission
from users.serializers import *

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        queryset = CustomUser.objects.all()
        s = UserSerializer(instance=queryset, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = UserSerializer(data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'error:数据有误'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, UserDetailViewPermission]

    def get(self,request, pk):
        user = request.user if pk == 0 else CustomUser.objects.get(pk=pk)
        s = UserSerializer(instance=user)  # 序列化用户对象
        return Response(data=s.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user if pk == 0 else CustomUser.objects.get(pk=pk)
        s = UserSerializer(instance=user, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = CustomUser.objects.get(id=pk)
        if not user:
            return Response(data={'error': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response(status=status.HTTP_200_OK)