#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 09:57:16
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'text']
