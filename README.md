# DesafioAlfa
Para executar primeiro instale:
    pip install django
    pip install celery
    pip install yfinance
    pip install django-celery
    pip install djangorestframework
    sudo apt install redis

Para poder enviar emails:
    Crie um arquivo /followShares/config.py:
    substituindo suas senhas:
        secretKey='sua chave secreta do django'
        emailHostUser='seu email que será usado para enviar os emails'
        emailHostPassword='a apps password desse email' (pode fazer ela em https://security.google.com/settings/security/apppasswords, qualquer duvida me mande um email e eu envio o meu config.py com minhas senhas para vocês testarem)

Para executar:
    rode em 3 abas do terminal dentro da pasta do projeto:
    1o terminal executa: "python manage.py runserver 8080" (ou qualquer outra porta)
    2o terminal executa: "redis-server"
    3o terminal executa: "celery -A followShares worker -l info"

agora no ser browser busque: "http://localhost:8080" (substituindo 8080 pela porta usada)
nessa pagina voce pode visualizar e adicionar acoes a serem acompanhadas e adicionar emails para receberem notificacoes se o valor de alguma delas sair do valor do tunel buscado

para parar a execucao do celery worker que envia os emails e atualiza os valores das acoes execute (senao vai continuar com o processo rodando e enviando emails):
    pkill -f celery