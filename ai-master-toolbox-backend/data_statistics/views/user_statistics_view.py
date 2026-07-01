from datetime import datetime

from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api_log.models import APIAccessLog
from data_statistics.serializers import PerDayDataSerializer
from data_statistics.util import get_per_day_list_by_query_set
from users.models import CustomUser


class UserTotalCountView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        count = CustomUser.objects.count()
        return Response(data={'count': count}, status=status.HTTP_200_OK)

class ActiveUserPerDayCountView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        """
        需要传递的参数： {
            start_time,
            end_time : end_time默认截止到当前时间
        }
        :param request:
        :return:
        """
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

        query_set = APIAccessLog.objects.filter(timestamp__range=(start_time, end_time))
        query_set = query_set.annotate(date=TruncDate('timestamp')).\
            values('date').\
            annotate(count=Count('user_id', distinct=True))

        result = get_per_day_list_by_query_set(start_time, end_time, query_set)

        s = PerDayDataSerializer(data=result, many=True)
        if s.is_valid():
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

class NewUserPerDayCountView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        """
        需要传递的参数： {
            start_time,
            end_time : end_time默认截止到当前时间
        }
        :param request:
        :return:
        """
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

        query_set = APIAccessLog.objects.filter(
            timestamp__range=(start_time, end_time),
            api_name='UserRegisterView',
            status_code=200
        )
        query_set = query_set.annotate(date=TruncDate('timestamp')).\
            values('date').\
            annotate(count=Count('id'))

        result = get_per_day_list_by_query_set(start_time, end_time, query_set)

        s = PerDayDataSerializer(data=result, many=True)
        if s.is_valid():
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)