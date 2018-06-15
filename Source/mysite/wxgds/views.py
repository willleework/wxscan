# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
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
@require_user_login('请登录')
def index(request):
    if userauth.is_user_login(request):
        return HttpResponse('首页测试')
    else:
        return HttpResponse('没有权限')


'''
设备信息查询
'''
@require_user_login('尚未登录，请先登录')
def devInfoQuery(request):
    # dev_id = 'zkysw_asia_xizang_0001'
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
    issucess = userauth.user_login(requset, requset.GET['username'], requset.GET['password'])
    resp = HttpResponseBase()
    if issucess:
        resp.status = 1000
        resp.info = '登录成功'
        cache.set(requset.GET['username'], 'haha', 20)
        print('cache value:' + cache.get(requset.GET['username']))
    else:
        resp.status = 2004
        resp.info = '登录失败'
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
用户登出
'''
def logout(request):
    userauth.user_logout(request)
    return HttpResponse('用户登出')