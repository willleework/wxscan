# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wxgds.models import DeviceInfo

from wxgds.utils.auth import userauth
import json


# Create your views here.
def index(request):
    if userauth.is_user_login(request):
        return HttpResponse('首页测试')
    else:
        return HttpResponse('没有权限')


# 查询设备信息
def devInfoQuery(request):
    # dev_id = 'zkysw_asia_xizang_0001'
    devid = request.GET['dev_id']
    print('query id :' + devid)
    dev = DeviceInfo.objects.get(dev_id=devid)
    resp = {'status': '0', 'errorinfo': '',
            'data': {'dev_id': dev.dev_id, 'dev_info': dev.dev_info, 'dev_status': dev.dev_status}}
    return HttpResponse(json.dumps(resp), content_type="application/json")

'''
# 验证用户权限
def userauthenticate(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('通过')
    else:
        return HttpResponse('不通过')
'''

#登录测试
def logintest(requset):
    issucess = userauth.user_login(requset, requset.GET['username'], requset.GET['password'])
    if issucess:
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败')


#登出测试
def logouttest(request):
    userauth.user_logout(request)
    return HttpResponse('用户登出')