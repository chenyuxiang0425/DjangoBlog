# models告诉Djang'o如何处理应用程序中储存的数据
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):  # Model为Django中一个定义模型基本功能的类，只有text和date_added两个属性
    '''用户学习的主题'''
    text = models.CharField(max_length=200)  # CharField————由字符和文本组成的数据，预留200个字符
    date_added = models.DateTimeField(auto_now_add=True)  # 传递实参auto_now_add，每当用户创建新主题，都将Django的date_added自动设置为当前日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # 告诉Django默认使用哪个属性来显示有关主题的信息，调用__str__来显示模型的简单表示
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text


class Entry(models.Model):
    '''学习某个主题的具体知识'''
    # ForeignKey是数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。
    # 每个主题创建时，都给它分配一个键。需要在两项数据中建立联系时，Django使用与每项信息相关联的键。
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()  # 不限制条目长度
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # Meta储存用于管理模型的额外信息
        verbose_name_plural = 'entries'  # 一个特殊属性，让Django在需要时使用entries来表示多个目录。若没有这个类，Django用entrys表示。

    # 告诉Django默认使用哪个属性来显示有关主题的信息，调用__str__来显示模型的简单表示
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text[:50] + '...'
