# -*- coding: utf-8 -*-
##########################
#装饰器
##########################

from django.http import HttpResponse
from wxgds.utils.auth import userauth
from functools import wraps

from django.core.cache import cache

from wxgds.utils.domanimodels.httpresponse import HttpResponseBase

def require_user_login(tips = '当前用户尚未登录！'):
    '''
    装饰器：只允许已登录的用户
    :param tips:提示信息
    :return:
    '''
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if not userauth.is_user_login(request):
                #没有登录，返回状态码2001
                print('username：'+ request.user.username.encode('utf-8'))
                print('autho: ' + '0' if request.user.is_authenticated else '1')
                print('AnonymousUser[%s].Method Not Allowed (%s): %s' % (request.user.username.encode('utf-8'), request.method, request.path))
                resp = HttpResponseBase()
                resp.status = 2001
                resp.info = tips
                return HttpResponse(resp.convertToJson(), content_type="application/json")
            return func(request, *args, **kwargs)
        return inner
    return decorator


def require_user_login_cache(tips = '当前用户尚未登录！'):
    '''
    装饰器：只允许已登录的用户
    :param tips:提示信息
    :return:
    '''
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            serverSessionno = cache.get(request.GET['username'])
            clientSessionno = request.GET['session_no']
            print('server: '+ serverSessionno)
            print('client: '+ clientSessionno)
            # print('cache data;'+user.username)
            if serverSessionno != clientSessionno:
            #if not userauth.is_user_login(request):
                #没有登录，返回状态码2001
                print('username：'+ request.user.username.encode('utf-8'))
                print('autho: ' + '0' if request.user.is_authenticated else '1')
                print('AnonymousUser[%s].Method Not Allowed (%s): %s' % (request.user.username.encode('utf-8'), request.method, request.path))
                resp = HttpResponseBase()
                resp.status = 2001
                resp.info = tips
                return HttpResponse(resp.convertToJson(), content_type="application/json")
            return func(request, *args, **kwargs)
        return inner
    return decorator