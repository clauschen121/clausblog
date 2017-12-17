from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from system.storage import ImageStorage
from PIL import Image
import os
from django.db.models.fields.files import ImageFieldFile
from clausblog.settings import MEDIA_ROOT
# Create your models here.


def make_thumb(path, x, y, width, height, rate, save_size):
    img = Image.open(path)
    orgwidth, orgheight = img.size
    width = width / rate
    height = height / rate
    x = x / rate
    y = y / rate
    if width > (orgwidth - x):
        width = orgwidth - x
    if height > (orgheight - y):
        height = orgheight - y
    img2 = img.crop((x, y, (width + x), (height + y)))
    img3 = img2.resize((save_size, save_size), Image.ANTIALIAS)
    return img3


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(max_length=200, blank=True)
    orgimg = models.ImageField(
        upload_to='images/head',
        storage=ImageStorage(),
        default='images/head/default.jpg'
    )
    headimg = models.ImageField(
        upload_to='images/head',
        blank=True,
        default='images/head/default.thumb.jpg'
    )
    img_x = models.IntegerField(default=0)
    img_y = models.IntegerField(default=0)
    img_w = models.IntegerField(default=200)
    img_h = models.IntegerField(default=200)
    img_r = models.FloatField(default=1)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save(self):
        super(UserProfile, self).save()
        base, ext = os.path.splitext(os.path.basename(self.orgimg.url))
        thumb_root = 'images/head/'
        initimg = make_thumb(
            os.path.join(MEDIA_ROOT, self.orgimg.name),
            self.img_x,
            self.img_y,
            self.img_w, self.img_h, self.img_r, 120)
        relatedpath = os.path.join(thumb_root, base + '.thumb' + ext)
        hipath = os.path.join(MEDIA_ROOT, relatedpath)
        initimg.save(hipath)
        self.headimg = ImageFieldFile(self, self.headimg, relatedpath)
        super(UserProfile, self).save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)
