from django.urls import path, include

from users.views.feedback_view import FeedBackReplyListView, FeedBackReplyDetailView, FeedbackListView, \
    FeedbackDetailView
from users.views.login_view import UserLoginView
from users.views.register_view import UserRegisterView, VerifyCodeView
from users.views.modifyuser_view import ModifyPasswordView
from users.views.modifyuser_view import ModifyUserView
from users.views.logout_view import ExitLoginView
from users.views.user_assets_view import UserAssetsDetailView
from users.views.user_view import UserListView, UserDetailView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name='login'),
    path("verify_code/", VerifyCodeView.as_view(), name='get_verify_code'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("modify_password/", ModifyPasswordView.as_view(), name='modify_password'),
    path("modify_user/",ModifyUserView.as_view(), name = 'modify_user'),
    path("logout/",ExitLoginView.as_view(), name = 'exit_login'),
    path("",UserListView.as_view(), name = 'UserListView'),
    path("<int:pk>/",UserDetailView.as_view(), name = 'UserDetailView'),
    path("<int:pk>/asset/",UserAssetsDetailView.as_view(), name = 'UserAssetsDetailView'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view()),
    path('feedback/', FeedbackListView.as_view()),
    path('feedback/<int:feedback_id>/reply/', FeedBackReplyListView.as_view()),
    path('feedback/<int:feedback_id>/reply/<int:reply_id>/', FeedBackReplyDetailView.as_view()),
]