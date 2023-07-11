# Stock Price Tracker

This web application allows you to follow the price of different shares and set price tunnels and recipients to be notified via email if the price exceeds or falls bellow certain values.

![web page](https://github.com/VictorLutes/DesafioAlfa/blob/main/page.png)
![email notifications](https://github.com/VictorLutes/DesafioAlfa/blob/main/emails.png)

To run, install:<br>
&emsp;    pip install djaDesafioAlfango<br>
&emsp;    pip install celery<br>
&emsp;    pip install yfinance<br>
&emsp;    pip install django-celery<br>
&emsp;    pip install djangorestframework<br>
&emsp;    sudo apt install redis<br>
<br>
To send emails:<br>
&emsp;    Create a file "followShares/config.py" substituting these variables with your keys:<br>
&emsp;&emsp;        secretKey='your django secret key'<br>
&emsp;&emsp;        emailHostUser='your email account that will be used to send emails'<br>
&emsp;&emsp;        emailHostPassword='apps password of this email' (can be created at https://security.google.com/settings/security/apppasswords)<br>
<br>

Create your local database running:<br>
&emsp;    python manage.py migrate --run-syncdb <br>

<br>
Run:<br>
&emsp;    "python manage.py runserver 8080" (or any other door)<br>
&emsp;    "redis-server --port 6379"<br>
&emsp;    celery -A followShares worker -B -l info"<br>

to view in browser access: "http://localhost:8080" (or the door you used)<br>
nessa pagina voce pode visualizar e adicionar acoes a serem acompanhadas e adicionar emails para receberem notificacoes se o valor de alguma delas sair do valor do tunel buscado<br>
<br>
to stop the execution of the celery worker run:<br>
&emsp;    pkill -f celery<br>
<br>
Project Structure<br>
&emsp;    followShares/followShares contains the config files and celery.py which configures the periodic job<br>
    <br>
&emsp;    followShares/follows contains the web page. Nessa pasta os arquivos mais importantes sao:<br>
&emsp;        The folder templates contains the html files<br>
&emsp;        views.py presents the different web pages<br>
&emsp;        models.py contains the models for stocks and recipients<br>
&emsp;        tasks.py que contains the task to periodically update the value of shares and send emails<br>
<br>

# Seguidor De Acoes
Entre na pasta principal followShares<br><br>
Para executar primeiro instale:<br>
&emsp;    pip install djaDesafioAlfango<br>
&emsp;    pip install celery<br>
&emsp;    pip install yfinance<br>
&emsp;    pip install django-celery<br>
&emsp;    pip install djangorestframework<br>
&emsp;    sudo apt install redis<br>
<br>
Para poder enviar emails:<br>
&emsp;    Crie um arquivo followShares/config.py:<br>
&emsp;    Com essas 3 variaveis, substituindo suas senhas:<br>
&emsp;&emsp;        secretKey='sua chave secreta do django'<br>
&emsp;&emsp;        emailHostUser='seu email que será usado para enviar os emails'<br>
&emsp;&emsp;        emailHostPassword='apps password desse email' (pode criar ela em https://security.google.com/settings/security/apppasswords)<br>
<br>

Crie a base de dados local rodando:<br>
&emsp;    python manage.py migrate --run-syncdb <br>

<br>
Para executar:<br>
&emsp;    rode em 3 abas do terminal dentro da pasta do projeto:<br>
&emsp;    1o terminal executa: "python manage.py runserver 8080" (ou qualquer outra porta)<br>
&emsp;    2o terminal executa: "redis-server --port 6379"<br>
&emsp;    3o terminal executa: "celery -A followShares worker -B -l info"<br>

agora no ser browser busque: "http://localhost:8080" (substituindo 8080 pela porta usada)<br>
nessa pagina voce pode visualizar e adicionar acoes a serem acompanhadas e adicionar emails para receberem notificacoes se o valor de alguma delas sair do valor do tunel buscado<br>
<br>
para parar a execucao do celery worker que envia os emails e atualiza os valores das acoes execute (senao vai continuar com o processo rodando e enviando emails):<br>
&emsp;    pkill -f celery<br>
<br>
Estrutura do projeto<br>
&emsp;    followShares/followShares é uma pasta com os arquivos de configuracao do projeto, alem do celery.py que guarda a configuracao da tarefa que ocorre a cada minuto<br>
    <br>
&emsp;    followShares/follows é uma pasta com os arquivos da pagina web e das tarefas a serem feitas. Nessa pasta os arquivos mais importantes sao:<br>
&emsp;        A pasta templates com os arquivos html para as views<br>
&emsp;        O arquivo views.py que faz a apresentacao das diferentes paginas<br>
&emsp;        O arquivo models.py que guarda os modelos das acoes e dos recipientes(emails)<br>
&emsp;        O arquivo tasks.py que contem a tarefa de atualizar as acoes e roda a cada minutos, atualizando as acoes a cada n minutos<br>
<br>
