from django.shortcuts import render, redirect
from .models import Stock, Recipient
from .form import StockForm, RecipientForm

def listItems(request):
    latest_stock_list = Stock.objects.all()
    latest_recipient_list = Recipient.objects.all()
    stockForm=StockForm()
    recipientForm=RecipientForm()
    context = {
        'stock_list': latest_stock_list,
        'stock_form': stockForm,
        'recipient_list': latest_recipient_list,
        'recipient_form': recipientForm,
    }
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/follows/')
    elif request.method=='PUT':
        print(request.PUT)
        form=RecipientForm(request.PUT)
        if form.is_valid():
            form.save()
            redirect('/follows/')
    return render(request, 'listItems.html', context)

def update_stock(request, pk):
    latest_stock = Stock.objects.get(id=pk)
    stockForm=StockForm(instance=latest_stock)
    context = {
        'stock_form': stockForm,
        'stock': latest_stock
    }
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST, instance=latest_stock)
        if form.is_valid():
            form.save()
            redirect('/follows')
    return render(request, 'formUpdate.html', context)

def delete_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    context = {
        'item': stock
    }
    if request.method=='POST':
        stock.delete()
        print(request.POST)
        redirect('/follows')
    return render(request, 'confirmDelete.html', context)


def delete_email(request, pk):
    email = Recipient.objects.get(id=pk)
    context = {
        'item': email
    }
    if request.method=='POST':
        email.delete()
        print(request.POST)
        redirect('/follows')
    return render(request, 'confirmDelete.html', context)

def add_recipient(request):
    recipientForm=RecipientForm()
    context = {
        'recipient_form': recipientForm,
    }
    if request.method=='POST':
        print(request.POST)
        form=RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/follows')
    return render(request, 'addEmail.html', context)