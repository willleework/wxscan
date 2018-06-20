# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from wxgds.models import DeviceInfo
from wxgds.utils.auth import userauth
from wxgds.utils.decorator.authdecorator import *
from wxgds.utils.domanimodels.httpresponse import *

import json

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
    resp = DevQueryHttpRsp()
    devid = request.GET['dev_id']
    print('query id :' + devid)
    try:
        dev = DeviceInfo.objects.get(dev_id=devid)
        if dev:
            resp.status = 1000
            resp.info = '成功'
            resp.dev_id = dev.dev_id
            resp.dev_info = dev.dev_info
            resp.dev_status = dev.dev_status
        else:
            resp.status = 3002
            resp.info = '数据不存在'
    except ObjectDoesNotExist as e:
        resp.status = 3002
        resp.info = '数据不存在'
    except Exception as e:
        resp.status = 3001
        resp.info = e
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
设备借出
'''
@require_user_login_cache('尚未登录，请先登录')
def borrowDevice(request):
    resp = HttpResponseBase()
    devid =  request.GET['dev_id']
    if(devid==None or devid.strip()==''):
        resp.status = 3000
        resp.info = '无效的设备号'
    try:
        dev = DeviceInfo.objects.get(dev_id=devid)
        if(dev and dev.dev_status=='1'):
            dev.dev_status = '2'
            dev.save()
            resp.status = 1000
            resp.info = '设备租借成功'
        else:
            resp.status = 3000
            resp.info = '该设备不可借出'
    except ObjectDoesNotExist as e:
        resp.status = 3002
        resp.info = '设备不存在'
    except Exception as e:
        resp.status = 3001
        resp.info = e
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
设备归还
'''
def returnDevice(request):
    resp = HttpResponseBase()
    devid =  request.GET['dev_id']
    if(devid==None or devid.strip()==''):
        resp.status = 3000
        resp.info = '无效的设备号'
        resp.status = 1000
        resp.info = '设备归还成功'
    try:
        dev = DeviceInfo.objects.get(dev_id=devid)
        if(dev and dev.dev_status=='2'):
            dev.dev_status = '1'
            dev.save()
        else:
            resp.status = 3000
            resp.info = '该设备不需归还'
    except ObjectDoesNotExist as e:
        resp.status = 3002
        resp.info = '设备不存在'
    except Exception as e:
        resp.status = 3001
        resp.info = e
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
用户注册
'''
@csrf_exempt
def register(request):
    regresult = userauth.user_register_wx(request)
    resp = HttpResponseBase()
    if regresult['success'] == 'true':
        resp.status = 1000
        resp.info = regresult['info']
    else:
        resp.status = 3000
        print('login errinfo:' + regresult['info'].decode('utf-8'))
        resp.info = regresult['info']
    return HttpResponse(resp.convertToJson(), content_type="application/json")


'''
用户登录（微信方式）
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
        #print('login errinfo:'+loginresult['info'])
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

