#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 21:37:15
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
