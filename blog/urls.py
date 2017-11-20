#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 07:49:03
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)$', views.article, name='article'),
]
