# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json

'''
http返回类型基类
所有返回到前台的数据继承自此类
用法：
rsp = httpResponseBase()
rsp.status = 1000 #正常返回，无错误
return rsp
'''
class HttpResponseBase():

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if not isinstance(value, int):
            raise ValueError('http状态码必须是整数!')
        if value < 0:
            raise ValueError('http状态码必须大于0!')
        self._status = value

    @property
    def info(self):
        return self._info
    @status.setter
    def info(self, value):
        if not isinstance(value, str):
            raise ValueError('http返回信息必须是字符串!')
        self._info = value

    @property
    def session_no(self):
        return self._session_no
    @session_no.setter
    def info(self, value):
        if not isinstance(value, str):
            raise ValueError('session_no信息必须是字符串!')
        self._session_no = value

    #类信息序列化
    def convertToJson(self):
        return  json.dumps(self, default = lambda obj: obj.__dict__)


'''
设备查询返回类
'''
class DevQueryHttpRsp(HttpResponseBase):
    @property
    def dev_id(self):
        return self._devid
    @dev_id.setter
    def dev_id(self, value):
        if not isinstance(value, str):
            raise ValueError('设备id必须是字符串!')
        self._devid = value

    @property
    def dev_info(self):
        return self._devinfo
    @dev_info.setter
    def dev_info(self, value):
        if not isinstance(value, str):
            raise ValueError('设备信息必须是字符串!')
        self._devid = value

    @property
    def dev_status(self):
        return self._devstatus
    @dev_status.setter
    def dev_status(self, value):
        if not isinstance(value, str) and len(value) == 1:
            raise ValueError('设备状态必须是char类型')
        self._devstatus = value
