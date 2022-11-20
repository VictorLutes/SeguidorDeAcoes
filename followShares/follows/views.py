from django.shortcuts import render, redirect
from .models import Stock, Recipient
from .form import StockForm, RecipientForm

def listItems(request):
    #pagina que lista todas as acoes, podendo atualizar e remover elas, podendo adicionar uma nova acao
    #e lista todos os emails podendo deletar eles ou adicionar um novo email
    latest_stock_list = Stock.objects.all()
    latest_recipient_list = Recipient.objects.all()
    stockForm=StockForm()
    context = {
        'stock_list': latest_stock_list,
        'stock_form': stockForm,
        'recipient_list': latest_recipient_list,
    }
    #se recebeu um post de uma nova acao salvo ela
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'listItems.html', context)

def update_stock(request, pk):
    #pagina para atualizar uma acao especifica
    latest_stock = Stock.objects.get(id=pk)
    stockForm=StockForm(instance=latest_stock)
    context = {
        'stock_form': stockForm,
        'stock': latest_stock
    }
    #se recebeu um post, salvo a acao atualizada
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST, instance=latest_stock)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'formUpdate.html', context)

def delete_stock(request, pk):
    #pagina para confirmar ou cancelar a remocao de uma acao
    stock = Stock.objects.get(id=pk)
    context = {
        'item': stock
    }
    #se recebo um post apago essa acao
    if request.method=='POST':
        stock.delete()
        print(request.POST)
        return redirect('/')
    return render(request, 'confirmDelete.html', context)


def delete_email(request, pk):
    #pagina para confirmar ou cancelar a remocao de um email
    email = Recipient.objects.get(id=pk)
    context = {
        'item': email
    }
    #se recebo um post apago esse email
    if request.method=='POST':
        email.delete()
        print(request.POST)
        return redirect('/')
    return render(request, 'confirmDelete.html', context)

def add_recipient(request):
    #pagina para adicionar um novo email
    recipientForm=RecipientForm()
    context = {
        'recipient_form': recipientForm,
    }
    #se recebo um post apago o email
    if request.method=='POST':
        print(request.POST)
        form=RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'addEmail.html', context)