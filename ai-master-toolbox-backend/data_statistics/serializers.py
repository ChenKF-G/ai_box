from rest_framework import serializers

class PerDayDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('date', 'count')

class PerDayChatUsageSerializer(serializers.Serializer):
    date = serializers.DateField()
    prompt_tokens = serializers.IntegerField()
    completion_tokens = serializers.IntegerField()

    class Meta:
        fields = ('date', 'prompt_tokens', 'completion_tokens')

