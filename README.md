# DesafioAlfa
Para executar primeiro instale:<br>
    pip install django<br>
    pip install celery<br>
    pip install yfinance<br>
    pip install django-celery<br>
    pip install djangorestframework<br>
    sudo apt install redis<br>
<br>
Para poder enviar emails:<br>
    Crie um arquivo followShares/config.py:<br>
    substituindo suas senhas:<br>
        secretKey='sua chave secreta do django'<br>
        emailHostUser='seu email que será usado para enviar os emails'<br>
        emailHostPassword='apps password desse email' (pode criar ela em https://security.google.com/settings/security/apppasswords, qualquer duvida me mande um email e eu envio o meu config.py com minhas senhas para vocês testarem)<br>
<br>
Para executar:<br>
    rode em 3 abas do terminal dentro da pasta do projeto:<br>
    1o terminal executa: "python manage.py runserver 8080" (ou qualquer outra porta)<br>
    2o terminal executa: "redis-server"<br>
    3o terminal executa: "celery -A followShares worker -l info"<br>

agora no ser browser busque: "http://localhost:8080" (substituindo 8080 pela porta usada)<br>
nessa pagina voce pode visualizar e adicionar acoes a serem acompanhadas e adicionar emails para receberem notificacoes se o valor de alguma delas sair do valor do tunel buscado<br>
<br>
para parar a execucao do celery worker que envia os emails e atualiza os valores das acoes execute (senao vai continuar com o processo rodando e enviando emails):<br>
    pkill -f celery<br>
<br>
Estrutura do projeto<br>
    followShares/followShares é uma pasta com os arquivos de configuracao do projeto, alem do celery.py que guarda a configuracao da tarefa que ocorre a cada minuto<br>
    <br>
    followShares/follows é uma pasta com os arquivos da pagina web e das tarefas a serem feitas. Nessa pasta os arquivos mais importantes sao:<br>
        A pasta templates com os arquivos html para as views<br>
        O arquivo views.py que faz a apresentacao das diferentes paginas<br>
        O arquivo models.py que guarda os modelos das acoes e dos recipientes(emails)<br>
        O arquivo tasks.py que contem a tarefa de atualizar as acoes e roda a cada minutos, atualizando as acoes a cada n minutos<br>
