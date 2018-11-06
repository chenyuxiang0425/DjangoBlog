'''定义learning_logs的URL模式'''
from django.urls import path  # 导入path函数，用其将URL映射到视图
from . import views  # 从当前urls.py模块的文件夹中导入视图
app_name = 'learning_logs'  # 定义命名空间
urlpatterns = [
    # 主页
    # + 第一个实参表示查找开头和末尾之间没有任何东西的url;
    # + 第二个是指定要调用的视图函数,
    #   如果请求的URL与前述正则表达式匹配，django将调用views.index;
    # + 第三个是将这个URL模式的名称指定为index，让我们能够在代码的其他地方引用他,
    #   当需要提供到这个主页的链接时，我们都将使用这个名称而不编写URL。
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path(r'topic/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面,与http://localhost:8000/new_entry/id/的URL匹配
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]

