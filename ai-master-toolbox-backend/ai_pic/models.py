from django.db import models

from users.models import CustomUser


# Create your models here.

class PhotoUrls(models.Model):
    class Meta:
        app_label = 'ai_pic'
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, help_text='所属用户')
    image = models.ImageField(upload_to='id_photo/',null=True,blank=True)
    watermarkerimage = models.ImageField(upload_to='id_photo/', null=True, blank=True)
    createtime = models.DateTimeField(auto_now_add=True)
