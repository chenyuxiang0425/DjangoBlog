from django.contrib import admin

from learning_logs.models import Topic, Entry  # 注册模型Topic

admin.site.register(Topic)  # 让Django通过管理网站管理我们的模型
admin.site.register(Entry)