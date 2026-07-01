from django.db import models
from django.utils import timezone
from users.models import CustomUser

# 对话模型
class Conversation(models.Model):
    title = models.CharField(max_length=50, blank=True, default='', help_text='聊天标题')
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, help_text='用户')
    timestamp = models.DateTimeField(auto_now_add=True, help_text='对话创建时间')
    class Meta:
        verbose_name = "对话"
        verbose_name_plural = verbose_name
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title

class ChatContent(models.Model):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('system', 'system'),
        ('assistant', 'assistant'),
    )
    content = models.CharField(max_length=4096, default=None, null=True, help_text='聊天内容')
    role = models.CharField(max_length=12, choices=ROLE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True, help_text='聊天内容创建时间')
    conversation = models.ForeignKey(to=Conversation,  on_delete=models.CASCADE, help_text='对话外键')

    class Meta:
        verbose_name = "聊天内容"
        verbose_name_plural = verbose_name
        ordering = ["timestamp"]

    def __str__(self):
        return self.content

class ChatUsage(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, help_text='用户外键')
    timestamp = models.DateTimeField(auto_now_add=True, help_text='使用时间')
    prompt_tokens = models.IntegerField(default=0, help_text='发送内容的token数')
    completion_tokens = models.IntegerField(default=0, help_text='返回内容的token数')


