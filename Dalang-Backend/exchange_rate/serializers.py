from rest_framework import serializers
from .models import ExchangeRate

class ExchangeRateSerializer(serializers.ModelSerializer):
    """
    ExchangeRate 모델을 직렬화하는 Serializer
    """
    class Meta:
        model = ExchangeRate
        fields = ['currency_unit', 'date', 'exchange_rate']  # 반환할 필드 명시