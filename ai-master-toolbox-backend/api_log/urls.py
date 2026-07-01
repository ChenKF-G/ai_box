from django.urls import path

from api_log.views import APIListView, APIUsagePerDayView

urlpatterns = [
    path("apis/", APIListView.as_view(), name='api_list_view'),
    path("api_usage/", APIUsagePerDayView.as_view(), name='api_usage_view'),
]