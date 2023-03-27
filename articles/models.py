import datetime
import jdatetime
from django.db import models
from django_jalali.db import models as jmodels
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify
from account.models import User


def slugify_function(content): return slugify(content, allow_unicode=True)


class IpAddress(models.Model):                                          # users ip address
    ip_address = models.GenericIPAddressField()


class Article(models.Model):
    parent = models.ForeignKey(
        'self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children')
    slug = AutoSlugField(
        populate_from=['title'],
        unique=True,
        allow_unicode=True,
        slugify_function=slugify_function,
        blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='article_app/images')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    jalali_created = jmodels.jDateField(auto_now_add=True, null=True)
    hits = models.ManyToManyField(IpAddress, blank=True, related_name="hits")
    allowing = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replay')
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=300)
    comment = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    jalali_created = jmodels.jDateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return f"{self.firstname} - {self.comment[:30]}... "
