#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 15:08:32
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.contrib.syndication.views import Feed
from .models import Article

class AllArticlesRssFeed(Feed):
	title = 'clauschen博客文章'
	link = '/'
	description = 'clauschen博客文章列表'

	def items(self):
		return Article.objects.all()

	def item_title(self, item):
		return '[%s] %s' % (item.category, item.title)	

	def item_description(self, item):
		return item.body

