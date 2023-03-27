from django.db import models


class ContactInformation(models.Model):
    phone = models.CharField(max_length=50)
    second_phone = models.CharField(max_length=50)
    third_phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    instagram = models.URLField(max_length=300, blank=True)
    whatsapp = models.URLField(max_length=300, blank=True)
    allowing = models.BooleanField(default=False)
