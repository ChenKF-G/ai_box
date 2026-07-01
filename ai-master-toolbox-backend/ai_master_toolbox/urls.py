"""
URL configuration for ai_master_toolbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

prefix = 'api/'

urlpatterns = [
    path(prefix + 'admin/', admin.site.urls),
    path(prefix + "docs/", include_docs_urls(title="AI大师工具箱api文档",
                                    description="AI大师工具箱api文档")),
    path(prefix + 'token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # 获取令牌
    path(prefix + 'token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  # 刷新令牌
    path(prefix + 'log/', include("api_log.urls")),
    path(prefix + 'statistics/', include("data_statistics.urls")),
    path(prefix + "user/", include("users.urls")),
    path(prefix + 'chat/', include("chatgpt.urls")),
    path(prefix + 'ai_pic/',include("ai_pic.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
