from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from system.storage import ImageStorage
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=200)
    headimg = models.ImageField(
        upload_to='images/head',
        storage=ImageStorage()
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)
