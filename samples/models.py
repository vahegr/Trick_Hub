from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='sample_app/images', null=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.title} - {self.url}'
