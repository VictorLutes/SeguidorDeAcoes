from django.db import models
from django.urls import reverse
import yfinance as yf

# Create your models here.
#modelo de uma acao, com a sigla, low e high do tunel, data que foi criada, minutos entre atualizacoes e valor atual
class Stock(models.Model):
    sigla = models.CharField(max_length=20)
    timeCreated = models.DateTimeField(auto_now_add=True)
    low = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    currentPrice = models.FloatField(default=1.0)
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.sigla

#modelo de recipientes, com um email para onde deve ser enviado as notificacoes
class Recipient(models.Model):
    email = models.EmailField(max_length=30)
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.email
    