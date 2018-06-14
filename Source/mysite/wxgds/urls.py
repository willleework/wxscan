from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'devInfoQuery/', views.devInfoQuery, name='devInfoQuery'),
    #url(r'authenticate/', views.userauthenticate, name='authenticate'),
    url(r'logintest/', views.logintest, name='logintest'),
    url(r'logouttest/', views.logouttest, name='logouttest'),
]