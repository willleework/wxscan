# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceInfo(models.Model):
    #设备ID，唯一索引
    dev_id = models.CharField(max_length=200)
    #设备信息
    dev_info = models.CharField(max_length=500)
    # 设备状态 ‘0’：未初始化，‘1’：正常，‘2’：借出，‘3’：不可用
    dev_status = models.CharField(max_length=1)