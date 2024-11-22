from rest_framework import serializers
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption
# Deposit
# Deposit 데이터 불러오기
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        # fields = ('dcls_month', 'kor_co_nm', 'fin_prdt_nm')
        read_only_fields = ('interest_user',)
# Deposit 옵션 데이터 가져오기
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields=('deposit_product',)

# Deposit 리스트 출력
class DepositListSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProduct
        fields = '__all__'
        # fields = ('id', 'dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'depositoption_set')
        read_only_fields = ('interest_user',)
    

# Deposit 상품 상세 정보 출력
class DepositDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct

# Saving
# Saving 데이터 불러오기
class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)

# Saving 옵션 데이터 가져오기
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields=('saving_product',)

# Saving 리스트 출력
class SavingListSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProduct
        fields = '__all__'
        # fields = ('id', 'dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'savingoption_set')
        read_only_fields = ('interest_user',)



class InterestDepositSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)
    # interest_user_cnt = serializers.RelatedField(source="DepositProduct.objects.interest_user")
    class Meta:
        model = DepositProduct
        fields = ('id', 'fin_prdt_cd', 'fin_prdt_nm', 'kor_co_nm', 'depositoption_set')

class InterestSavingSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)
    class Meta:
        model = SavingProduct
        fields = ('id', 'fin_prdt_cd', 'fin_prdt_nm', 'kor_co_nm', 'savingoption_set')

class DepositMonthSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'

        read_only_fields = ('interest_user',)

    def __init__(self, *args, **kwargs):
        self.save_trm = kwargs.pop('save_trm', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        depositoption_set = representation.pop('depositoption_set')

        # save_trm 조건에 맞는 옵션만 필터링
        filtered_options = [option for option in depositoption_set if option['save_trm'] == self.save_trm]
        representation['depositoption_set'] = filtered_options

        return representation
        

class SavingMonthSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)
    class Meta:
        model = SavingProduct
        fields = ('id', 'dcls_month', 'fin_prdt_cd', 'fin_co_no', 'kor_co_nm', 'fin_prdt_nm', 'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'join_member', 'etc_note', 'max_limit', 'depositoption_set',) 

        read_only_fields = ('interest_user',)

    def __init__(self, *args, **kwargs):
        self.save_trm = kwargs.pop('save_trm', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        savingoption_set = representation.pop('savingoption_set')

        # save_trm 조건에 맞는 옵션만 필터링
        filtered_options = [option for option in savingoption_set if option['save_trm'] == self.save_trm]
        representation['savingoption_set'] = filtered_options

        return representation
    
class DepositRecommendSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProduct
        fields = '__all__'

class SavingRecommendSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProduct
        fields = '__all__'