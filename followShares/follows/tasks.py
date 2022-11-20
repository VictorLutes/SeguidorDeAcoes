from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime,timezone, timedelta
from follows.models import Recipient
from follows.models import Stock
import yfinance as yf
from django.core.mail import send_mail
from django.conf import settings

#funcao que executa a cada um minuto, periodicamente atualizando as acoes e mandando emails se o valor esta fora do tunel
@shared_task(name='update_shares')
def update_shares():
    #recipient_list guarda todos os emails que foram adicionados pelo usuario para receberem notificacoes
    recipient_list=[]
    querieEmails=Recipient.objects.all()
    for recipient in querieEmails:
        recipient_list.append(recipient.email)
    queries=Stock.objects.all()
    for share in queries:
        timesince = datetime.now(timezone.utc) - share.timeCreated
        minutessince = int(timesince.total_seconds() / 60)
        print(minutessince%share.minutes)
        if(minutessince%share.minutes==0):#atualiza o valor da acao e envia email so a cada share.minutes minutos
            #atualiza currentPrice, o valor da acao usando o yahoo finance
            ticker = yf.Ticker(share.sigla).info
            share.currentPrice = ticker['regularMarketPrice']
            print(recipient_list)
            print('Ticker: ', share.sigla)
            print('Market Price:', share.currentPrice)
            print('Current value of stock: '+str(share.currentPrice)+', high value of tunnel: '+str(share.high)+', current time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)))
            #salva a alteracao no valor da acao
            share.save()
            #se o valor é ascima do que foi passado no limite superior do tunel, envio email para vender a acao
            if(share.high<share.currentPrice):
                print("send email sell")
                send_mail(
                    'sell stock: '+share.sigla,
                    'Current value of stock: '+str(share.currentPrice)+'\nHigh value of tunnel: '+str(share.high)+'\nCurrent time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)),
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                    fail_silently=False
                )
            #se o valor é abaixo do que foi passado no limite inferior do tunel, envio email para comprar a acao
            if(share.currentPrice<share.low):
                print("send email buy")
                send_mail(
                    'buy stock: '+share.sigla,
                    'Current value of stock: '+str(share.currentPrice)+'\nLow value of tunnel: '+str(share.low)+'\nCurrent time: '+str(datetime.now(timezone.utc)-timedelta(hours=3)),
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                    fail_silently=False
                )
    return 