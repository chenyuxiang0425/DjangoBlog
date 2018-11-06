# 根据信息自动创建表单
from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):  # TopicForm继承了forms.ModelForm
    class Meta:  # 最简单的ModelForm只包含一个内嵌的Meta类，Meta类指定了根据哪个模型创建表单，以及在表单中包含哪些字段。
        model = Topic  # 根据模型Topic创建一个表单
        fields = ['text']  # 该表单只包含字段text
        labels = {'text': ''}  # 不用为字段text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
