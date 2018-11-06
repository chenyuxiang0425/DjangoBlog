# 告诉Django应创建哪些网页来响应浏览器请求
"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin

# urlpatterns包含项目中的应用程序和URL
urlpatterns = [
    path('admin/', admin.site.urls),  # admin.site.urls模块定义了可在管理网站中请求的所有URL
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),  # 实参namespace能够将learning_logs的URL同项目中的其他URL区分开来。
]

