from rest_framework import status
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from chatgpt.models import Conversation
from chatgpt.serializers import ConversationSerializer


@throttle_classes([UserRateThrottle])
class ConversationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query_set = Conversation.objects.filter(user=request.user)
        s = ConversationSerializer(instance=query_set, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request):
        converstaion = Conversation.objects.create(title='无标题', user=request.user)
        s = ConversationSerializer(instance=converstaion)
        return Response(data=s.data, status=status.HTTP_200_OK)

class ConversationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        converstaion = Conversation.objects.get(pk=pk)
        if converstaion.user.id != request.user.id:
            return Response(data={'error:该会话不属于您'}, status=status.HTTP_400_BAD_REQUEST)
        s = ConversationSerializer(instance=converstaion, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = Conversation.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)