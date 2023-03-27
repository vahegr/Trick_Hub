from django.db import models


class About(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='about_app/images', null=True)

    def __str__(self):
        return f'{self.title} - {self.description[:30]}...'
