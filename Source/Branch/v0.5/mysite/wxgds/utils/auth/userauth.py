# -*- coding: utf-8 -*-
#################################
# 用户权限认证模块
#################################
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # 权限相关
from django.core.cache import cache

import json
import requests

from wxgds.utils.common import commonhelper
from wxgds.utils.domanimodels.reporitory import UserBase
from wxgds.models import Operator
##################################

'''
用户登录，本地方式
'''
def user_login(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        # 密码认证成功，登录
        login(request, user)
        #生成缓存信息并保存到cache里，用于下次请求认证
        cachUser = commonhelper.getUserInfoFromRequest(request)
        cache.set(request.session.session_key, cachUser.convertToJson(), 60*60*12)#token有效12小时
        print('user[%s] login success!sessionid[%s]' % (cachUser.user_name, request.session.session_key))
        return True
    else:
        # 密码认证失败，返回false
        return False



'''
用户注册，微信方式
'''
def user_register_wx(request):
    jscode = request.POST.get('jscode', None)
    nickname = request.POST.get('nickname', None)
    if jscode == None:
        return {'success': 'false', 'info': '无效的用户信息{null}'}
    print('get user info ;' +jscode.decode('utf-8'))
    res = GetWxUsrSession(jscode)
    openid = None
    #获取微信openid信息
    if(res.has_key('openid')):
        openid = res['openid']
    # 判断openid是否有效
    if openid == None or openid.strip() == '':
        errinf = ''
        if res.has_key('errmsg'):
            errinf =  res['errmsg']
        print('[%s]user login failed: %s' % (jscode, errinf))
        return {'success':'false', 'info':errinf}
    else:
        opes = Operator.objects.filter(open_id=openid);
        if(len(opes)>0):
            return {'success': 'false', 'info': '用户已存在'}
        else:
            Operator.objects.create(open_id=openid, nick_name=nickname)
            return {'success': 'true', 'info': '用户注册申请成功，请等待审核'}


'''
用户登录，微信方式
'''
def user_login_wx(request, jscode):
    res = GetWxUsrSession(jscode)
    openid = None
    #获取微信openid信息
    if(res.has_key('openid')):
        openid = res['openid']
    #判断openid是否有效
    if openid== None or openid.strip()=='':
        errinf = ''
        if res.has_key('errmsg'):
            errinf =  res['errmsg']
        #print('[%s]user login failed: %s' % (jscode, errinf.decode('utf-8')))
        return {'success':'false', 'info':errinf}
    else:
        #微信登录成功，进行本地操作员认证，暂未实现授权模块
        ope = Operator.objects.get(open_id=openid)
        if not ope == None and ope.status=='1':
            # 生成缓存信息并保存到cache里，用于下次请求认证维护session
            cachUser = UserBase()
            cachUser.open_id = ope.open_id
            cachUser.user_name = ope.nick_name
            cache.set(res['session_key'], cachUser.convertToJson(), 60*60*12)#token有效12小时
            return {'success': 'true',  'info': '登录成功', 'session_key':res['session_key']}
        else:
            return {'success': 'false',  'info': '操作员用户信息认证失败'}


#用户登出
def user_logout(request):
    #logout(request)
    cache.delete(request.GET['session_no'])  # 退出后删除tocken
    print('sessionid[%s] is delete' % request.GET['session_no'])


#用户是否登录
def is_user_login(request):
    return  request.user.is_authenticated


#获取微信账户信息
def GetWxUsrSession(jscode):
    try:
        url = 'https://api.weixin.qq.com/sns/jscode2session'
        data = {
            'grant_type': 'authorization_code',
            'appid': 'wxffbbad03a07971af',
            'secret': '4a3c26bf103d1e12de1fb18085bd9be8',
            'js_code': jscode
        }
        res = requests.get(url=url, params=data)
        return res.json()
    except Exception as e:
        res = {'errcode':'wxrerr', 'errmsg' : e}
        return res



