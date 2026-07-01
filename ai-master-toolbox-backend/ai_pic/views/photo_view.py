import uuid
from io import BytesIO

from ai_pic.permissions import IdPhotoViewPermission
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import FileResponse
from users.models import UserAssets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rembg import remove
from ai_pic.models import *
import os
import copy
from PIL import Image, ImageDraw, ImageFont

def watermark(img):
    # 创建画布
    draw = ImageDraw.Draw(img)
    # 设置字体
    font_path = os.path.join(os.path.dirname(__file__), '王金彦简行书.ttf')
    font = ImageFont.truetype(font_path, 30)
    # 设置水印文本
    text = 'AI大师工具箱'
    # 设置文本颜色
    text_color = (255, 255, 255)
    # 获取图片尺寸
    width, height = img.size
    # 计算文本位置
    text_x = width - 240
    text_y = height - 160
    # 绘制水印文本
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    # 保存图片
    return img

class ChangePhotoBackgroundView(APIView):
    permission_classes = [IdPhotoViewPermission]

    def post(self, request):
        if 'photo' in request.FILES:
            input_path = request.FILES['photo']
            size = request.POST.get('sizelist')
            color = request.POST.get('colorlist')  #'0,0,255'
            colorlist = [int(x) for x in color.split(',')]
            sizelist = [int(x) for x in size.split(',')]
            R = colorlist[0]
            G = colorlist[1]
            B = colorlist[2]
            colors = (R,G,B)
            replacement_color = colors

            inch_to_w = sizelist[0]
            inch_to_h = sizelist[1]

            # 使用rembg去除背景
            input_image = Image.open(input_path)
            output_image = remove(input_image)

            # 创建一个新图像，将透明背景替换
            replacement_image = Image.new("RGBA", output_image.size, replacement_color)
            result_image = Image.alpha_composite(replacement_image, output_image)

            width = int(inch_to_w)  # 将宽度转换为像素
            height = int(inch_to_h)  # 将高度转换为像素

            # 调整图像大小
            new_size = (width, height)  # 设置新的尺寸
            result_image = result_image.resize(new_size)  #result_image：更换完底色的图片

            # 创建result_image的副本
            watermark_image = copy.copy(result_image)

            # 添加水印到副本上
            watermark_image = watermark(watermark_image)

            # 将图像保存为字节流
                #原始
            image_stream = BytesIO()
            result_image.save(image_stream, format='png')
                #水印
            watermark_stream = BytesIO()
            watermark_image.save(watermark_stream, format='png')

            # 生成一个随机的文件名
            filename = f'image_{request.user.id}_{uuid.uuid4()}.png'
            watermarkfilename = 'watermark' + str(filename)

            # 将字节流转换为Django文件对象
            image_file = InMemoryUploadedFile(image_stream, None, filename, 'image/png',
                                              image_stream.getbuffer().nbytes, None)
            watermarkimage_file = InMemoryUploadedFile(watermark_stream, None, watermarkfilename, 'image/png',
                                              watermark_stream.getbuffer().nbytes, None)

            try:
                old_photoUrl = PhotoUrls.objects.filter(user=request.user).order_by('-createtime')[:1].get()
                if old_photoUrl:
                    file = str(old_photoUrl.image)
                    name_without_extension = file.split('/')[1]
                    imagefile_path = str('media/id_photo/' + name_without_extension + '/')
                    watermarkfile_path = str('media/id_photo/' + 'watermark' + name_without_extension + '/')
                    os.remove(str(imagefile_path))
                    os.remove(str(watermarkfile_path))
            except ObjectDoesNotExist:
                pass

            # 存入数据库
            PhotoUrls.objects.create(user =request.user,image = image_file, watermarkerimage = watermarkimage_file)

            # 获取路径
            photoUrl = PhotoUrls.objects.filter(user=request.user).order_by('-createtime')[:1].get()
            watermarkurlpath = str('/api/media/') + str(photoUrl.watermarkerimage)

            # 构造响应数据
            data = {'watermarkimage_url':watermarkurlpath}

            # 创建响应对象
            return Response(data=data, status=status.HTTP_200_OK)

        return Response({'error': '请传入照片'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if  not request.user.is_superuser:
            object = UserAssets.objects.get(user=request.user)
            if object.idphoto_count <= 0 :
                return Response({'error': '请获取下载次数'}, status=status.HTTP_400_BAD_REQUEST)
            object.idphoto_count -= 1
            object.save()
        photo = PhotoUrls.objects.filter(user=request.user).order_by('-createtime')[:1].get()
        filename = str(photo.image.file.name)
        response = FileResponse(open(filename, 'rb'))
        return response
