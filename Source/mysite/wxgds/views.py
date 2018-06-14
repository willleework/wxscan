# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wxgds.models import DeviceInfo
#权限相关
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def index(request):
    return HttpResponse('首页测试')

#查询设备信息
def devInfoQuery(request):
    #dev_id = 'zkysw_asia_xizang_0001'
    devid =  request.GET['dev_id']
    print('query id :' + devid)
    dev = DeviceInfo.objects.get(dev_id=devid)
    resp = {'status':'0', 'errorinfo':'', 'data': {'dev_id': dev.dev_id, 'dev_info': dev.dev_info, 'dev_status': dev.dev_status}}
    return HttpResponse(json.dumps(resp), content_type="application/json")

'''
#验证用户权限
def userauthenticate(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('通过')
    else:
        return HttpResponse('不通过')

def querydata(request):
    return HttpResponse('通过权限认证');

def logindenid():
    return HttpResponse('访问被拒绝');
'''


