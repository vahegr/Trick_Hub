from django.db import models


class PlanFeature(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Plan(models.Model):
    title = models.CharField(max_length=300)
    development_tool = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=2000)
    price = models.CharField(max_length=100)
    simple = models.BooleanField(default=False)
    feature = models.ManyToManyField(PlanFeature)

    def __str__(self):
        return f"{self.title} - {self.price}"
