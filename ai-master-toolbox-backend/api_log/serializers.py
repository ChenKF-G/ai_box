from rest_framework import serializers

from api_log.models import APIAccessLog


class APIUsageSerializer(serializers.Serializer):
    api_name = serializers.CharField()
    method = serializers.CharField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('api_name', 'method', 'count')

class UsageByDaySerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('date', 'count')
