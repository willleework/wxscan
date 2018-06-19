# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceInfo(models.Model):
    #设备ID，唯一索引
    dev_id = models.CharField(max_length=200, primary_key=True)
    #设备信息
    dev_info = models.CharField(max_length=500)
    # 设备状态 ‘0’：未初始化，‘1’：正常，‘2’：借出，‘3’：不可用
    dev_status = models.CharField(max_length=1, default='0')


class Operator(models.Model):
    #微信openid，用户唯一标识
    open_id = models.CharField(max_length=200, primary_key=True)
    #微信昵称
    nick_name = models.CharField(max_length=500, default='')
    #权限分组，暂未使用
    groupid = models.CharField(max_length=50, default='0')
    #状态 ‘0’：未认证， ‘1’：通过认证， '2'：未通过认证
    status = models.CharField(max_length=1, default='0')
    #备注
    remark = models.CharField(max_length=500, default='')