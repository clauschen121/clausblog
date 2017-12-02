from django.db import models
from system.storage import ImageStorage

# Create your models here.


class UploadImage(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(
        upload_to='images',
        height_field='height',
        width_field='width',
        storage=ImageStorage()
    )
    height = models.PositiveIntegerField(default=200)
    width = models.PositiveIntegerField(default=300)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
    	return self.name
