import requests
import random
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DepositSerializer, DepositOptionSerializer, DepositListSerializer, InterestDepositSerializer, DepositRecommendSerializer
from .serializers import SavingSerializer, SavingOptionSerializer, SavingListSerializer, InterestSavingSerializer, SavingRecommendSerializer
from .models import DepositProduct, SavingProduct, DepositOption, SavingOption
from accounts.models import User

API_KEY = "8fbfa11f9a3138d46e386c74e602fbd0"

@api_view(['GET'])
def get_deposit_products(request):
    deposit_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    deposit_baselist = requests.get(deposit_API_URL).json().get('result').get('baseList')
    deposit_optionlist = requests.get(deposit_API_URL).json().get('result').get('optionList')

    # return Response(deposit_baselist)   

    for base in deposit_baselist:
        if DepositProduct.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')):
            continue
        deposit_product = {
            'dcls_month' : base.get('dcls_month'),
            'fin_prdt_cd': base.get('fin_prdt_cd'),
            'fin_co_no': base.get('fin_co_no'),
            'kor_co_nm': base.get('kor_co_nm'),
            'fin_prdt_nm': base.get('fin_prdt_nm'),
            'join_way': base.get('join_way'),
            'mtrt_int': base.get('mtrt_int'),
            'spcl_cnd': base.get('spcl_cnd'),
            'join_deny': base.get('join_deny'),
            'join_member': base.get('join_member'),
            'etc_note': base.get('etc_note'),
            'max_limit': base.get('max_limit')
        }
        serializer = DepositSerializer(data=deposit_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    # return Response(deposit_baselist)
    for option in deposit_optionlist:
        prdt_cd = option.get('fin_prdt_cd')
        products = DepositProduct.objects.filter(fin_prdt_cd=prdt_cd)
        for product in products:
            deposit_option = {
                'intr_rate_type': option.get('intr_rate_type'),
                'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                'save_trm': option.get('save_trm'),
                'intr_rate': option.get('intr_rate'),
                'intr_rate2': option.get('intr_rate2'),
            }
            serializer = DepositOptionSerializer(data=deposit_option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(deposit_product=product)
                # return Response(deposit_option)
    return Response('Deposit 데이터 가져오기 성공')



@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo='

    for page in range(1, 11):  # pageNo 1부터 10까지
        response = requests.get(f"{saving_API_URL}{page}").json()
        saving_result = response.get('result', {})
        saving_baselist = saving_result.get('baseList', [])
        saving_optionlist = saving_result.get('optionList', [])

        if not saving_baselist:  # 데이터가 없으면 다음 페이지로 넘어감
            continue

        for base in saving_baselist:
            if SavingProduct.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')).exists():
                continue
            saving_product = {
                'dcls_month': base.get('dcls_month'),
                'fin_prdt_cd': base.get('fin_prdt_cd'),
                'fin_co_no': base.get('fin_co_no'),
                'kor_co_nm': base.get('kor_co_nm'),
                'fin_prdt_nm': base.get('fin_prdt_nm'),
                'join_way': base.get('join_way'),
                'mtrt_int': base.get('mtrt_int'),
                'spcl_cnd': base.get('spcl_cnd'),
                'join_deny': base.get('join_deny'),
                'join_member': base.get('join_member'),
                'etc_note': base.get('etc_note'),
                'max_limit': base.get('max_limit')
            }
            serializer = SavingSerializer(data=saving_product)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        for option in saving_optionlist:
            prdt_cd = option.get('fin_prdt_cd')
            products = SavingProduct.objects.filter(fin_prdt_cd=prdt_cd)
            for product in products:
                saving_option = {
                    'intr_rate_type': option.get('intr_rate_type'),
                    'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                    'rsrv_type': option.get('rsrv_type'),
                    'rsrv_type_nm': option.get('rsrv_type_nm'),
                    'save_trm': option.get('save_trm'),
                    'intr_rate': option.get('intr_rate'),
                    'intr_rate2': option.get('intr_rate2'),
                }
                serializer = SavingOptionSerializer(data=saving_option)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(saving_product=product)

    return Response('Saving 데이터 가져오기 성공')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_product_list(request):
    if request.method == 'GET':
        deposit_products = DepositProduct.objects.all()
        serializer = DepositListSerializer(deposit_products, many=True)
        return Response(serializer.data)
    
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def saving_product_list(request):
    if request.method == 'GET':
        saving_products = SavingProduct.objects.all()
        serializer = SavingListSerializer(saving_products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def deposit_detail(request, deposit_name):
    deposit = get_object_or_404(DepositProduct, fin_prdt_nm=deposit_name)
    if request.method == 'GET':
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_detail(request, saving_name):
    saving = get_object_or_404(SavingProduct, fin_prdt_nm=saving_name)
    if request.method == 'GET':
        serializer = SavingSerializer(saving)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_option_list(request, deposit_name):
    deposit = get_object_or_404(DepositProduct, fin_prdt_nm=deposit_name)
    deposit_options = DepositOption.objects.filter(deposit_product=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_option_detail(request, deposit_code, option_id):
    deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
    option = DepositOption.objects.get(deposit_product=deposit, id=option_id)
    if request.method == 'GET':
        serializer = DepositOptionSerializer(option)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_option_list(request, saving_name):
    saving = get_object_or_404(SavingProduct, fin_prdt_nm=saving_name)
    saving_options = SavingOption.objects.filter(saving_product=saving)

    if request.method == 'GET':
        serializer = SavingOptionSerializer(saving_options, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_option_detail(request, saving_code, option_id):
    saving = get_object_or_404(SavingProduct, fin_prdt_cd=saving_code)
    option = SavingOption.objects.get(saving_product=saving, id=option_id)
    if request.method == 'GET':
        serializer = SavingOptionSerializer(option)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bank_deposit(request, bank_name):
    if request.method == 'GET':
        if DepositProduct.objects.filter(kor_co_nm=bank_name).exists():
            deposits = DepositProduct.objects.filter(kor_co_nm=bank_name)
            serializer = DepositListSerializer(deposits, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': '해당 은행의 상품이 없습니다.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bank_saving(request, bank_name):
    if request.method == 'GET':
        if SavingProduct.objects.filter(kor_co_nm=bank_name).exists():
            savings = SavingProduct.objects.filter(kor_co_nm=bank_name)
            serializer = SavingListSerializer(savings, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': '해당 은행의 상품이 없습니다.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_deposit(request, deposit_code):
    deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
    user = request.user
    if deposit.interest_user.filter(id=user.id).exists():
        deposit.interest_user.remove(user)  # 이미 좋아요한 경우 좋아요 취소
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    else:
        deposit.interest_user.add(user)  # 좋아요 추가
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_saving(request, saving_code):
    saving = get_object_or_404(SavingProduct, fin_prdt_cd=saving_code)
    user = request.user
    if saving.interest_user.filter(id=user.id).exists():
        saving.interest_user.remove(user)  # 이미 좋아요한 경우 좋아요 취소
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    else:
        saving.interest_user.add(user)  # 좋아요 추가
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_recommend(request, username):
    user = get_object_or_404(User, username=username)
    salary = user.salary
    wealth = user.wealth
    tendency = user.tendency
    desirePeriod = user.desirePeriod

    deposits = user.deposit.all()
    cnt_lst = [0] * 70
    
    users = User.objects.all()
    for user in users:
        if (salary-10000000 <= user.salary <= salary+10000000) \
            and (wealth-1000000000 <= user.wealth <= wealth+100000000) \
            and (tendency-2 <= user.tendency <= tendency+2)\
            and (desirePeriod-12 <= user.desirePeriod <= desirePeriod+12):
            deposits = user.deposit.all()
            for deposit in deposits:
                cnt_lst[int(deposit.id)] += 1
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    cnt_tpl.sort(key= lambda x: -x[0])
    # print(cnt_tpl)
    best = []
    for i in range(5):
        best.append(cnt_tpl[i][1])
    # print(best)
    deposits = DepositProduct.objects.filter(id__in=best)
    serializer = DepositRecommendSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_recommend(request, username):
    user = get_object_or_404(User, username=username)
    salary = user.salary
    wealth = user.wealth
    tendency = user.tendency
    desirePeriod = user.desirePeriod

    savings = user.saving.all()
    cnt_lst = [0] * 70
    
    users = User.objects.all()
    for user in users:
        if (salary-10000000 <= user.salary <= salary+10000000) \
            and (wealth-1000000000 <= user.wealth <= wealth+100000000) \
            and (tendency-2 <= user.tendency <= tendency+2)\
            and (desirePeriod-12 <= user.desirePeriod <= desirePeriod+12):
            savings = user.saving.all()
            for saving in savings:
                cnt_lst[int(saving.id)] += 1
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    cnt_tpl.sort(key= lambda x: -x[0])
    # print(cnt_tpl)
    best = []
    for i in range(5):
        best.append(cnt_tpl[i][1])
    # print(best)
    savings = SavingProduct.objects.filter(id__in=best)
    serializer = SavingRecommendSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_recommend_second(request, username):
    user = get_object_or_404(User, username=username)
    age = user.age
    deposits = user.deposit.all()
    cnt_lst = [0] * 70
    users = User.objects.all()
    for user in users:
        if age // 10 == user.age // 10:
            deposits = user.deposit.all()
            for deposit in deposits:
                cnt_lst[int(deposit.id)] += 1
    # print(cnt_lst)
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    # print(cnt_tpl)
    cnt_tpl.sort(key= lambda x: -x[0])
    best = []
    for i in range(5):
        best.append(cnt_tpl[i][1])
    # print(best)
    deposits = DepositProduct.objects.filter(id__in=best)
    serializer = DepositRecommendSerializer(deposits, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_recommend_second(request, username):
    user = get_object_or_404(User, username=username)
    age = user.age
    savings = user.saving.all()
    cnt_lst = [0] * 70
    users = User.objects.all()
    for user in users:
        if age // 10 == user.age // 10:
            savings = user.saving.all()
            for saving in savings:
                cnt_lst[int(saving.id)] += 1
    # print(cnt_lst)
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    # print(cnt_tpl)
    cnt_tpl.sort(key= lambda x: -x[0])
    best = []
    for i in range(5):
        best.append(cnt_tpl[i][1])
    savings = SavingProduct.objects.filter(id__in=best)
    serializer = SavingRecommendSerializer(savings, many=True)
    return Response(serializer.data)