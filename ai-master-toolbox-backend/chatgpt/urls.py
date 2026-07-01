from django.urls import path

from chatgpt.views.chat_content_view import ChatContentListView, ChatResponseForAnswerView, ChatResponseForTitleView
from chatgpt.views.conversation_view import ConversationListView, ConversationDetailView

urlpatterns = [
    path("conv/", ConversationListView.as_view(), name="conversation_list_view"),
    path("conv/<int:pk>/", ConversationDetailView.as_view(), name="conversation_detail_view"),
    path("conv/<int:pk>/chat_cont/", ChatContentListView.as_view(), name="chat_content_list_view"),
    path("conv/<int:pk>/chat_resp/", ChatResponseForAnswerView.as_view(), name="chat_response_view"),
    path("conv/<int:pk>/chat_title/", ChatResponseForTitleView.as_view(), name="chat_response_view"),
]