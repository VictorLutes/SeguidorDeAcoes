from rest_framework import serializers
from follows.models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields=['sigla', 'timeCreated', 'low', 'high', 'minutes', 'currentPrice']