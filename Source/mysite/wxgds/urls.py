from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'devInfoQuery/', views.devInfoQuery, name='devInfoQuery'),
    url(r'login/', views.login, name='login'),
    url(r'logout/', views.logout, name='logout'),
]