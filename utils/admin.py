from django.contrib import admin
from .models import UploadImage
# Register your models here.


@admin.register(UploadImage)
class UploadImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'height', 'width', 'created_time']
