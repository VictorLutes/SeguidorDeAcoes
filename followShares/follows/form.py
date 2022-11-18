from .models import Stock, Recipient
from django.forms import ModelForm

class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields=['sigla', 'low', 'high', 'minutes']

class RecipientForm(ModelForm):
    class Meta:
        model=Recipient
        fields=['email']