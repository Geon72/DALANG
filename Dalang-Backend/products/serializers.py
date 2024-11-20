from rest_framework import serializers
from .models import DepositProduct, SavingProduct

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'  # 모든 필드를 포함


class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'  # 모든 필드를 포함
