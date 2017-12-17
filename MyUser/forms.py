#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 21:44:05
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.forms import ModelForm, Textarea, TextInput, EmailInput, PasswordInput, FileInput, HiddenInput
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder': '密码',
                   'style': 'background:url(/static/user/images/password.png) no-repeat 10px'}
        ),
    )

    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder': '确认密码',
                   'style': 'background:url(/static/user/images/password.png) no-repeat 10px'}
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'placeholder': '用户名', 'style': 'background:url(/static/user/images/username.png) no-repeat 10px;'}),
            'email': EmailInput(attrs={'placeholder': '邮箱', 'style': 'background:url(/static/user/images/email.png) no-repeat 10px;'})
        }


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['description', 'orgimg', 'img_x',
                  'img_y', 'img_w', 'img_h', 'img_r']
        widgets = {'description': Textarea(attrs={'placeholder': '一句话描述你自己吧!', 'rows': 5, 'style': 'background:url(/static/user/images/description.png) no-repeat 10px'}),
                   'orgimg': FileInput(attrs={'accept': 'image/gif,image/jpeg,image/jpg,image/png,image/svg', 'onchange': 'imageClip(this)'}),
                   'img_x': HiddenInput(),
                   'img_y': HiddenInput(),
                   'img_w': HiddenInput(),
                   'img_h': HiddenInput(),
                   'img_r': HiddenInput(),
                   }
