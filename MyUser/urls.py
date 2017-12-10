#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-06 13:37:24
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url('^register/$', views.register, name='register'),
]
