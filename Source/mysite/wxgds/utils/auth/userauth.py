# -*- coding: utf-8 -*-
#################################
# 用户权限认证模块
#################################
from django.http import HttpResponse
# 权限相关
from django.contrib.auth import authenticate, login, logout


##################################

# 用户登录
# request,
# username, 用户名
# password, 密码
def user_login(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        # 密码认证成功，登录
        login(request, user)
        return True
    else:
        # 密码认证失败，返回false
        return False


#用户登出
def user_logout(requset):
    logout(requset)


#用户是否登录
def is_user_login(request):
    return  request.user.is_authenticated