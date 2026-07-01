from datetime import datetime, timedelta

from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api_log.models import APIAccessLog
from api_log.serializers import APIUsageSerializer, UsageByDaySerializer
from data_statistics.serializers import PerDayDataSerializer
from data_statistics.util import get_per_day_list_by_query_set


# Create your views here.

class APIListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        query_set = APIAccessLog.objects.values('api_name', 'method').\
            annotate(count=Count('id')).\
            order_by('-count')
        s = APIUsageSerializer(instance=query_set, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

class APIUsagePerDayView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        """
        需要传递的参数： {
            api_name,
            method,
            start_time,
            end_time : end_time默认截止到当前时间
        }
        :param request:
        :return:
        """
        api_name = request.data.get('api_name', '')
        method = request.data.get('method', '')
        start_time = request.data.get('start_time', '2023-10-01 00:00:00')
        end_time = request.data.get('end_time', '')
        try:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            if end_time:
                end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            else:
                end_time = timezone.now()
        except Exception as e:
            return Response(data={'error': '时间格式错误'}, status=status.HTTP_400_BAD_REQUEST)

        if start_time >= end_time:
            return Response(data={'error': '开始时间超过结束时间'}, status=status.HTTP_400_BAD_REQUEST)

        query_set = APIAccessLog.objects.filter(api_name=api_name, method=method)

        if not query_set.exists():
            return Response(data={'error': '没有该api的使用记录'}, status=status.HTTP_400_BAD_REQUEST)

        query_set = query_set.filter(timestamp__range=(start_time, end_time))

        query_set = query_set.annotate(date=TruncDate('timestamp') ).\
            values('date').\
            annotate(count=Count('id')).order_by('date')

        result = get_per_day_list_by_query_set(start_time, end_time, query_set)

        s = PerDayDataSerializer(instance=result, many=True)

        return Response(data=s.data, status=status.HTTP_200_OK)



