#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 21:44:05
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.forms import ModelForm, Textarea
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['description', 'headimg']
        widgets = {'description': Textarea(attrs={'rows': 5})}
