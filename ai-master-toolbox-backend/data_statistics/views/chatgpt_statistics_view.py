from datetime import datetime
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from chatgpt.models import ChatUsage
from data_statistics.serializers import PerDayChatUsageSerializer
from data_statistics.util import get_date_range


class TokenUsagePerDayCountView(APIView):
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

        query_set = ChatUsage.objects.filter(timestamp__range=(start_time, end_time))
        query_set = query_set.annotate(date=TruncDate('timestamp')).\
            values('date').\
            annotate(
                prompt_tokens = Sum('prompt_tokens'),
                completion_tokens = Sum('completion_tokens')
            ).order_by('date')

        date_range = get_date_range(start_time, end_time)
        # 创建一个字典来存储结果
        result_dict = {}
        # 将实际数据与日期范围内的所有日期合并，确保不存在的日期 count 设置为 0
        for entry in query_set:
            date = entry['date']
            prompt_tokens = entry['prompt_tokens']
            completion_tokens = entry['completion_tokens']
            result_dict[date] = {
                'prompt_tokens': prompt_tokens,
                'completion_tokens': completion_tokens
            }
        for date in date_range:
            if date not in result_dict:
                result_dict[date] = {
                    'prompt_tokens': 0,
                    'completion_tokens': 0
                }

        result = [{'date': k,
                   'prompt_tokens': result_dict[k]['prompt_tokens'],
                   'completion_tokens': result_dict[k]['completion_tokens']
                   } for k in result_dict]
        result.sort(key=lambda e: e['date'])

        s = PerDayChatUsageSerializer(data=result, many=True)
        if s.is_valid():
            return Response(data=s.data, status=status.HTTP_200_OK)
        else:
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


