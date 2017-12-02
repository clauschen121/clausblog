from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.


class Category(models.Model):
    '''
    文章分类：字段为name
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    文章标签：字段为name
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    '''
    文章内容结构
    标题，内容，创建时间，修改时间，摘要，图片，分类，标签，作者
    '''

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    image = models.ForeignKey('utils.UploadImage')

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)
    slider = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Article, self).save(*args, **kwargs)

