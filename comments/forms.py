#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 09:57:16
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django import forms
from .models import Comment, Commentme
from django.forms import Textarea


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'text']
        widgets = {
            'text': Textarea(attrs={
                'placeholder': '支持markdown格式留言,最多只能输入1000字',
                'onKeyDown': 'textCounter(1000);',
                'onKeyUp': 'textCounter(1000);'
            })
        }


class CommentMeForm(forms.ModelForm):

    class Meta:
        model = Commentme
        fields = ['user', 'text']
        widgets = {
            'text': Textarea(attrs={
                'placeholder': '支持markdown格式留言,最多只能输入1000字',
                'onKeyDown': 'textCounter(1000);',
                'onKeyUp': 'textCounter(1000);'
            })
        }
