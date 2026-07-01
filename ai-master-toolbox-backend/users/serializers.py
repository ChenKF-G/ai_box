import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser, UserAssets, Feedback, FeedbackReply, FeedbackImage


def validate_phone(value):
    pattern = r'^1\d{10}$'
    return bool(re.match(pattern, value))

def validate_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, value))

def validate_username(value):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern,value))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password']

    phone = serializers.CharField(validators=[validate_phone])

    def create(self, validated_data):
        password = validated_data.pop('password', '123456')
        email = validated_data.pop('email', '')
        username = email
        instance = CustomUser(
            username = username,
            password = make_password(password),
            email = email)
        return instance

class UserAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssets
        fields = '__all__'

class FeedbackImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackImage
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    images = FeedbackImageSerializer(many=True, required=False)
    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        images_data = request.FILES.getlist('images')  # 获取上传的文件列表

        images_data = self.validate_images(images_data)

        feedback = Feedback.objects.create(
            user=request.user,
            title=validated_data['title'],
            content=validated_data['content'])

        for image_data in images_data:
            FeedbackImage.objects.create(feedback=feedback, image=image_data)

        return feedback

    def validate_images(self, value):
        # 自定义验证逻辑，例如验证文件数量和大小
        max_file_count = 5  # 最大文件数量
        max_file_size = 2 * 1024 * 1024  # 最大文件大小（2MB）

        if len(value) > max_file_count:
            raise serializers.ValidationError(f'最多只能上传 {max_file_count} 个文件。')

        for image_data in value:
            if image_data.size > max_file_size:
                raise serializers.ValidationError(
                    f'文件 "{image_data.name}" 太大，不能超过 2MB。')

        return value

class FeedbackReplySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    feedback = serializers.ReadOnlyField(source='feedback.id')
    class Meta:
        model = FeedbackReply
        fields = '__all__'