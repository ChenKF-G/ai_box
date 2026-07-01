from django.urls import path, include

from ai_pic.views.photo_view import ChangePhotoBackgroundView

urlpatterns = [
    path("id_photo/", ChangePhotoBackgroundView.as_view(), name='photo'),
]