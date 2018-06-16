# -*- coding: utf-8 -*-
#################################
# 用户权限认证模块
#################################
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # 权限相关
from django.core.cache import cache

from wxgds.utils.common import commonhelper
from wxgds.utils.domanimodels.reporitory import UserBase
##################################

'''
用户登录
'''
def user_login(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        # 密码认证成功，登录
        login(request, user)
        #生成缓存信息并保存到cache里，用于下次请求认证
        cachUser = commonhelper.getUserInfoFromRequest(request)
        cache.set(request.session.session_key, cachUser.convertToJson(), 60*60*12*7) #token有效7天
        print('user[%s] login success!sessionid[%s]' % (cachUser.user_name, request.session.session_key))
        return True
    else:
        # 密码认证失败，返回false
        return False


#用户登出
def user_logout(request):
    #logout(request)
    cache.delete(request.GET['session_no'])  # 退出后删除tocken
    print('sessionid[%s] is delete' % request.GET['session_no'])


#用户是否登录
def is_user_login(request):
    return  request.user.is_authenticated


