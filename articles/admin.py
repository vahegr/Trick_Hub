from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.IpAddress)
admin.site.register(models.Like)
admin.site.register(models.Comment)
