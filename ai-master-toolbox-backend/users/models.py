import random

from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # Add your custom fields here

    phone = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        help_text=_('手机号'))

    user_level = models.IntegerField(default=0, help_text="用户等级，0代表普通用户")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ["-user_level", "email"]

class UserAssets(models.Model):
    user = models.OneToOneField(to=CustomUser,  on_delete=models.CASCADE, help_text='用户外键')
    invite_code = models.IntegerField(default=10000000, unique=True, help_text="用户的邀请码")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    chatgpt_expired_time = models.DateTimeField(default=timezone.now, help_text="chatgpt的过期时间")
    chatgpt_left_count = models.IntegerField(default=0, help_text="chatgpt剩余使用次数")
    idphoto_count = models.IntegerField(default=0, help_text="下载证件照剩余使用次数")

class FeedbackImage(models.Model):
    image = models.ImageField(upload_to='feedback_images/')

class Feedback(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, help_text='所属用户')
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=512)
    images = models.ManyToManyField(to=FeedbackImage, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, help_text='反馈创建时间')
    handled = models.BooleanField(default=False, help_text='是否已经处理')

    class Meta:
        verbose_name = "反馈"
        verbose_name_plural = verbose_name
        ordering = ["-timestamp"]

class FeedbackReply(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, help_text='所属用户')
    feedback = models.ForeignKey(to=Feedback, on_delete=models.CASCADE, help_text='所属反馈')
    content = models.TextField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True, help_text='反馈创建时间')
    handled = models.BooleanField(default=False, help_text='是否已经处理')

    class Meta:
        verbose_name = "反馈的回复"
        verbose_name_plural = verbose_name
        ordering = ["-timestamp"]







