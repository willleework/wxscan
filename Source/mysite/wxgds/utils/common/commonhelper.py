# -*- coding: utf-8 -*-
import json

from wxgds.utils.domanimodels.reporitory import UserBase

'''
从request中获取用户信息
'''
def getUserInfoFromRequest(request):
    user = UserBase()
    if request.method == 'GET':
        user.user_name = request.GET['username']
        user.pass_word = request.GET['password']
    elif request.method == 'POST':
        temp = request.POST.get('user', None)
        user.user_name = temp.username
        user.pass_word = temp.password
    else:
        return None
    return user

'''
是否为json数据
'''
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True
