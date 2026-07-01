from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Feedback, FeedbackReply
from users.permissions import FeedBackPermission, FeedBackRepleyPermission
from users.serializers import FeedbackSerializer, FeedbackReplySerializer

class FeedbackListView(APIView):
    permission_classes = [FeedBackPermission]

    def get(self, request):
        query_set =  Feedback.objects.all() \
            if request.user.is_superuser \
            else Feedback.objects.filter(user=request.user)
        s = FeedbackSerializer(instance=query_set, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = FeedbackSerializer(data=request.data, partial=True, context={'request': request})
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetailView(APIView):
    permission_classes = [FeedBackPermission]
    def get(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        s = FeedbackSerializer(instance=feedback)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        s = FeedbackSerializer(instance=feedback, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        feedback.delete()
        return Response(status=status.HTTP_200_OK)

class FeedBackReplyListView(APIView):
    permission_classes = [FeedBackRepleyPermission]
    def get(self, request, feedback_id):
        feedback = Feedback.objects.get(id=feedback_id)
        replys_set = FeedbackReply.objects.filter(feedback=feedback)
        s = FeedbackReplySerializer(instance=replys_set, many=True)  # 序列化用户对象
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request, feedback_id):
        feedback = Feedback.objects.get(id=feedback_id)
        s = FeedbackReplySerializer(data=request.data, partial=True)
        if s.is_valid():
            s.save(feedback=feedback, user=request.user)
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

class  FeedBackReplyDetailView(APIView):
    permission_classes = [FeedBackRepleyPermission]

    def put(self, request, feedback_id, reply_id):
        feedback = Feedback.objects.get(id=feedback_id)
        reply = FeedbackReply.objects.get(id=reply_id)
        if not feedback or not reply:
            return Response(data={'error': '资源不存在'}, status=status.HTTP_400_BAD_REQUEST)
        s = FeedbackReplySerializer(instance=reply, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feedback_id, reply_id):
        feedback = Feedback.objects.get(id=feedback_id)
        reply = FeedbackReply.objects.get(id=reply_id)
        if not feedback or not reply:
            return Response(data={'error': '资源不存在'}, status=status.HTTP_400_BAD_REQUEST)
        reply.delete()
        return Response(status=status.HTTP_200_OK)
