# models.py

from django.db import models

class APIAccessLog(models.Model):
    user_id = models.IntegerField(null=True)
    api_name = models.CharField(max_length=30)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    parameters = models.CharField(max_length=255)
    status_code = models.PositiveIntegerField()
    response_data = models.CharField(max_length=512, null=True, blank=True)
    processing_time = models.IntegerField(help_text='api处理时间，单位ms')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user:{self.user_id} call {self.api_name}, {self.method}, {self.path}, {self.timestamp}"
