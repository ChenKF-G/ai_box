from rest_framework import serializers
from chatgpt.models import Conversation, ChatContent, ChatUsage

class ConversationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Conversation
        fields = '__all__'

class ChatContentDetailSerializer(serializers.ModelSerializer):
    conversation = serializers.ReadOnlyField(source='conversation.id')

    class Meta:
        model = ChatContent
        fields = '__all__'

class ChatContentOnlySerializer(serializers.ModelSerializer):
    """
    只有核心内容， openai 不允许有额外字段
    """
    class Meta:
        model = ChatContent
        fields = ('role', 'content')

class ChatUsageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = ChatUsage
        fields = '__all__'




