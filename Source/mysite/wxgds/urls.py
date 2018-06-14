from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'devInfoQuery/', views.devInfoQuery, name='devInfoQuery'),
    url(r'authenticate/', views.userauthenticate, name='authenticate'),
]