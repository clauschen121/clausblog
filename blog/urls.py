#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 07:49:03
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$',
        views.ArticleView.as_view(), name='article'),
    url(r'^article/likes/',
        views.ArticleLikes, name='articlelikes'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',
        views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^author/(?P<pk>[0-9]+)/$',
        views.AuthorView.as_view(), name='author'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^donate/$', views.Donate, name='donate')
]
