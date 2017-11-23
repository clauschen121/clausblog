#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 11:26:56
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/article/(?P<article_pk>[0-9]+)/$',
        views.article_comment, name='article_comment')
]
