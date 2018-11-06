from django.shortcuts import render, get_object_or_404  # render()函数根据视图提供的数据渲染响应
from django.http import HttpResponseRedirect, Http404  # 用户提交主题后使用HttpResponseRedirect类将用户重定向到网页topics
from django.urls import reverse  # 函数reverse()根据指定的URL模式确定URL，即django将在页面被请求时生成URL
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    '''学习笔记的主页'''
    # 这里的函数render()提供了两个实参：
    # 原始请求对象以及一个可用于创建网页的模板。
    return render(request, 'learning_logs/index.html')


# 使用 @login_required 限制访问。
# 加上装饰器（ @login_required ）之后，python会在运行 topics()的代码前先运行 login_required()的代码。
# login_required()会检查用户是否已登录，仅当用户已登录时，django才运行topics()。
# 如果未登录，就重定向到登录页面。 为实现重定向，需要修改 setting.py。
@login_required
def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # 查询数据库————请求提供Topic对象，并按属性date_added对它们进行排序。我们把返回的查询集储存在topics中。
    context = {'topics': topics}  # 定义一个将要发送给模板的上下文，上下文为一个字典，键：我们将在模板中用来访问数据的名称；值：我们要发送给模板的数据。
    return render(request, 'learning_logs/topics.html', context)  # 对象request，模板的路径，变量context


@login_required
def topic(request, topic_id):
    '''显示单个主题及其所有的条目'''
    topic = get_object_or_404(Topic, id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')  # -表示降序
    context = {'topic': topic, 'entries': entries}  # 主题和条目都储存在字典context中
    return render(request, 'learning_logs/topic.html', context)  # 将字典发送至模板topic.html中


@login_required
def new_topic(request):  # 请求对象作为参数
    '''添加新主题'''
    if request.method != 'POST':  # 初次请求浏览器发送'GET'请求
        # 未提交数据：创建一个新表单
        form = TopicForm()  # 返回一个空表单，供用户填写
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)  # 根据用户输入的数据在request.POST创建一个实例，该form含有用户的数据
        if form.is_valid():  # 输入数据与要求的字段路径一致
            new_topic =form.save(commit=False)  # 表单数据写入数据库
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # 使用reverse获取页面topics的URL

    context = {'form': form}  # 将这个表单发送给模板
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    '''在特定的主题种添加新条目'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':  # 初次请求浏览器发送'GET'请求
        # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)  # 根据用户输入的数据在request.POST创建一个实例，该form含有用户的数据
        if form.is_valid():  # 输入数据与要求的字段路径一致
            new_entry = form.save(commit=False)  # 让Django创建一个新的条目对象，并将其储存到new_entry中，但不将它保存到数据库中。
            new_entry.topic = topic  # 将new_entry的属性topic设置为在这个函数开头从数据库获取的主题
            new_entry.save()  # 保存到数据库中，与正确的主题相关联
            # 在调用reserve()时需要提供两个实参。
            # 第一个是根据它来生成URL的URL模式的名称。
            # 第二个是列表args，其中存储着要包含在URL中的所有实参。
            # 用户提交主题后使用HttpResponseRedirect类将用户重定向到新增条目所属的页面
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    '''编辑既有条目'''
    entry = Entry.objects.get(id=entry_id)  # 获取用户需要修改的条目对象，以及与该条目相关联的主题。
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        # 使用实参instance=entry创建EntryForm实例。
        # 这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。
        # 用户看到既有数据，并且能编辑他们。
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        # 让Django根据既有条目对象创建一个表单实例，并根据request.POST中的相关数据对其进行修改。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))  # 重定向到显示条目所属主题的页面

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)