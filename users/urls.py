'''定义users的URL模式'''
from django.urls import path  # 导入path函数，用其将URL映射到视图
from django.contrib.auth.views import LoginView  # 导入默认视图login
from . import views  # 从当前urls.py模块的文件夹中导入视图

urlpatterns = [
        # 登陆界面
        path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # 告诉Django去哪里查找我们将编写的模板
        # 注销
        path('logout/', views.logout_view, name='logout'),
        # 注册
        path('register/', views.register, name='register'),
]

app_name = 'users'  # 定义命名空间
