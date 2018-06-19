# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session

from wxgds.models import DeviceInfo
from wxgds.utils.auth import userauth
from wxgds.utils.decorator.authdecorator import *
from wxgds.utils.domanimodels.httpresponse import *

import json

from django.core.cache import cache


# Create your views here.
'''
首页函数（web）
'''
@require_user_login_cache('尚未登录，请先登录')
def index(request):
    resp = HttpResponseBase()
    if userauth.is_user_login(request):
        #resp.session_no = sessionid
        resp.status = 1000
        resp.info = '首页测试'
        return HttpResponse(resp.convertToJson(), content_type="application/json")
    else:
        return HttpResponse('没有权限')


'''
设备信息查询
'''
@require_user_login_cache('尚未登录，请先登录')
def devInfoQuery(request):
    devid = request.GET['dev_id']
    print('query id :' + devid)
    dev = DeviceInfo.objects.get(dev_id=devid)
    resp = DevQueryHttpRsp()
    resp.status = 1000
    resp.info = '成功'
    resp.dev_id = dev.dev_id
    resp.dev_info = dev.dev_info
    resp.dev_status = dev.dev_status
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
用户登录
'''
def login(requset):
    loginresult = userauth.user_login_wx(requset, requset.GET['jscode'])
    resp = HttpResponseBase()
    if loginresult['success'] == 'true':
        resp.status = 1000
        resp.info = '登录成功'
        resp.session_no = loginresult['session_key']
    else:
        resp.status = 2004
        resp.info = loginresult['info']
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
用户登出
'''
def logout(request):
    #username = request.user.username
    userauth.user_logout(request)
    #print("用户[%s]退出" % username)
    resp = HttpResponseBase()
    resp.status = 1000
    resp.info = '用户退出成功'
    return HttpResponse(resp.convertToJson(), content_type="application/json")

