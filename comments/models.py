from django.db import models
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey('MyUser.Userprofile')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('blog.Article')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.text[:20]


class Commentme(models.Model):
    user = models.ForeignKey('MyUser.Userprofile')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.text[:20]
