#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 11:41:23
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121

from django import template
from ..models import Article, Category

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
