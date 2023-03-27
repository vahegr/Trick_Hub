from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    icon = models.ImageField(upload_to='service_app/images')

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'
