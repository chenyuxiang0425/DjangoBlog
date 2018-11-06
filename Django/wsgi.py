# 帮助Djang'o提供它创建的文件，即web server gateway interface(web服务器网关接口)
"""
WSGI config for Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # 导入静态文件的Cling


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Django.settings')
application = Cling(get_wsgi_application())  # 使用Cling来启动程序

