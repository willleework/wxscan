# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wxgds.models import DeviceInfo
import json

# Create your views here.
def index(request):
    return HttpResponse('项目测试')

#查询设备信息
def devInfoQuery(request):
    #dev_id = 'zkysw_asia_xizang_0001'
    devid =  request.GET['dev_id']
    print('query id :' + devid)
    dev = DeviceInfo.objects.get(dev_id=devid)
    resp = {'status':'0', 'errorinfo':'', 'data': {'dev_id': dev.dev_id, 'dev_info': dev.dev_info, 'dev_status': dev.dev_status}}
    return HttpResponse(json.dumps(resp), content_type="application/json")