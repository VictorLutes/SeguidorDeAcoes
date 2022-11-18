"""followShares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listItems, name='list'),
    path('update_stock/<str:pk>/', views.update_stock, name='update_stock'),
    path('delete_stock/<str:pk>/', views.delete_stock, name='delete_stock'),
    path('delete_email/<str:pk>/', views.delete_email, name='delete_email'),
    path('add_recipient/', views.add_recipient, name='add_recipient'),
]
