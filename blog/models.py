from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    '''
    文章分类：字段为name
    '''
    name = models.CharField(max_length=100)


class Tag(models.Model):
    '''
    文章标签：字段为name
    '''
    name = models.CharField(max_length=100)


class Article(models.Model):
    '''
    文章内容结构
    标题，内容，创建时间，修改时间，摘要，图片，分类，标签，作者
    '''

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=100)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
