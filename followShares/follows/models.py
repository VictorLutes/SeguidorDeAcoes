from django.db import models
from django.urls import reverse

# Create your models here.

class Stock(models.Model):
    sigla = models.CharField(max_length=20)
    timeCreated = models.DateTimeField(auto_now_add=True)
    low = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    currentPrice = models.FloatField(default=0.0)
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.sigla

class Recipient(models.Model):
    email = models.CharField(max_length=30)
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.email
    