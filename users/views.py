from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm  # 默认表单
from django.shortcuts import render


def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))  # 返回主页


def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登陆，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])  # 要求被输两次密码
            login(request, authenticated_user)  # 为新用户创建有效的会话
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)