from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime,timezone, timedelta
from follows.models import Recipient
from follows.models import Stock
import yfinance as yf
from django.core.mail import send_mail
from django.conf import settings

@shared_task(name='update_shares')
def update_shares():
    recipient=[]
    queries=Recipient.objects.all()
    for i in queries:
        recipient.append(queries.email)
    queries=Stock.objects.all()
    for share in queries:
        timesince = datetime.now(timezone.utc)+timedelta(hours=3, minutes=30) - share.timeCreated
        minutessince = int(timesince.total_seconds() / 60)

        if(minutessince%share.minutes==0):
            #update currentPrice
            ticker = yf.Ticker(share.sigla).info
            market_price = ticker['regularMarketPrice']
            print(recipient)
            print('Ticker: ', share.sigla)
            print('Market Price:', market_price)
            print('Current value of stock: '+str(share.currentPrice)+', high value of tunnel: '+str(share.high)+', current time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)))
            share.currentPrice=market_price
            share.save()
            if(share.high<share.currentPrice):
                print("send email sell")
                send_mail(
                    'sell stock: '+share.sigla,
                    'Current value of stock: '+str(share.currentPrice)+'\nHigh value of tunnel: '+str(share.high)+'\nCurrent time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)),
                    settings.EMAIL_HOST_USER,
                    recipient,
                    fail_silently=False
                )
            if(share.currentPrice<share.low):
                print("send email buy")
                send_mail(
                    'buy stock: '+share.sigla,
                    'Current value of stock: '+str(share.currentPrice)+'\nLow value of tunnel: '+str(share.low)+'\nCurrent time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)),
                    settings.EMAIL_HOST_USER,
                    recipient,
                    fail_silently=False
                )
    return 