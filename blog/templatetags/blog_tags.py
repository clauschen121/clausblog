#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 11:41:23
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121

from django import template
from django.db.models.aggregates import Count
from ..models import Article, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)


@register.simple_tag
def get_tags():
	return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)


@register.simple_tag
def get_sliders(num=5):
	return Article.objects.all().filter(slider=True)[:num]