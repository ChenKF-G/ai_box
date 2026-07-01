from django.urls import path

from data_statistics.views.chatgpt_statistics_view import TokenUsagePerDayCountView
from data_statistics.views.user_statistics_view import UserTotalCountView, ActiveUserPerDayCountView, \
    NewUserPerDayCountView

urlpatterns = [
    path("user/total/", UserTotalCountView.as_view(), name='UserTotalCountView'),
    path("user/active_pd/", ActiveUserPerDayCountView.as_view(), name='ActiveUserPerDayCountView'),
    path("user/new_pd/", NewUserPerDayCountView.as_view(), name='NewUserPerDayCountView'),
    path("chat/token_pd/", TokenUsagePerDayCountView.as_view(), name='TokenUsagePerDayCountView')
]