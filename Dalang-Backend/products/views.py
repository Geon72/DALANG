from rest_framework import generics
from .models import DepositProduct, SavingProduct
from .serializers import DepositProductSerializer, SavingProductSerializer

class DepositProductListView(generics.ListAPIView):
    """
    정기 예금 전체 데이터를 반환하는 뷰
    """
    queryset = DepositProduct.objects.all()
    serializer_class = DepositProductSerializer


class DepositProductDetailView(generics.RetrieveAPIView):
    """
    특정 정기 예금 데이터를 반환하는 뷰
    """
    queryset = DepositProduct.objects.all()
    serializer_class = DepositProductSerializer


class SavingProductListView(generics.ListAPIView):
    """
    적금 전체 데이터를 반환하는 뷰
    """
    queryset = SavingProduct.objects.all()
    serializer_class = SavingProductSerializer


class SavingProductDetailView(generics.RetrieveAPIView):
    """
    특정 적금 데이터를 반환하는 뷰
    """
    queryset = SavingProduct.objects.all()
    serializer_class = SavingProductSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DepositProduct, SavingProduct
from .serializers import DepositProductSerializer, SavingProductSerializer
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

class RecommendProductsView(APIView):
    """
    사용자 정보를 바탕으로 정기 예금 및 적금 추천
    """
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id query parameter is required."}, status=400)

        # 사용자 정보 로드
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

        # 사용자 특성
        age = user.age
        tendency = user.tendency
        salary = user.salary
        wealth = user.wealth
        gender = user.gender
        
        ## 건아 부탁한다 ^^ ##
        # 정기 예금 추천
        deposit_products = DepositProduct.objects.filter(
            Q(join_deny="1") |  # 제한 없음
            Q(join_deny="2")  # 서민전용 조건 충족
        ).order_by('-intr_rate2')[:10]

        # 적금 추천
        saving_products = SavingProduct.objects.filter(
            Q(join_deny="1") |  # 제한 없음
            Q(join_deny="2")  # 서민전용 조건 충족
        ).order_by('-intr_rate2')[:10]

        # 직렬화
        deposit_serializer = DepositProductSerializer(deposit_products, many=True)
        saving_serializer = SavingProductSerializer(saving_products, many=True)

        # 응답
        return Response({
            "user": {
                "username": user.username,
                "age": user.age,
                "gender": "Male" if user.gender == 1 else "Female",
                "salary": user.salary,
                "wealth": user.wealth,
                "tendency": user.tendency,
            },
            "deposit_products": deposit_serializer.data,
            "saving_products": saving_serializer.data,
        }, status=200)



# 시중은행 예금 상품 데이터 from 금융감독원 정기예금 API
import requests
from django.shortcuts import render
from .models import DepositProduct
from .models import SavingProduct

def fetch_and_store_deposit_products(request):
    # 금융감독원 API URL
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    api_key = "8fbfa11f9a3138d46e386c74e602fbd0"
    topFinGrpNo = "020000"  # 은행 그룹 코드 (시중은행)

    total_data = []  # 데이터를 담을 리스트

    try:
        # 여러 페이지에 걸쳐 데이터를 가져오기
        for page in range(1, 4):  # pageNo를 1부터 3까지 반복
            params = {
                "auth": api_key,
                "topFinGrpNo": topFinGrpNo,
                "pageNo": str(page),
                "numOfRows": "100"  # 100개의 데이터를 가져옵니다
            }
            # API 요청
            response = requests.get(url, params=params)
            data = response.json()

            # 응답 데이터에서 baseList 항목 가져오기
            products = data.get("result", {}).get("baseList", [])
            options = data.get("result", {}).get("optionList", [])
            
            # 데이터를 결합하여 저장
            combined_data = zip(products, options)
            total_data.extend(combined_data)

        # 각 상품 데이터를 데이터베이스에 저장
        for product, option in total_data:
            DepositProduct.objects.create(
                kor_co_nm=product.get("kor_co_nm", ""),
                fin_prdt_nm=product.get("fin_prdt_nm", ""),
                intr_rate_type=option.get("intr_rate_type", ""),
                save_trm=option.get("save_trm", ""),
                intr_rate=float(option.get("intr_rate", 0) or 0),
                intr_rate2=float(option.get("intr_rate2", 0) or 0),
                join_way=product.get("join_way", ""),
                spcl_cnd=product.get("spcl_cnd", ""),
                join_deny=product.get("join_deny", ""),
                join_member=product.get("join_member", ""),
                etc_note=product.get("etc_note", "")
            )

        # 성공 메시지를 템플릿에 전달
        return render(request, 'products/success.html', {'message': '데이터가 성공적으로 저장되었습니다.'})

    except Exception as e:
        # 오류 발생 시 에러 메시지를 템플릿에 전달
        return render(request, 'products/error.html', {'error': str(e)})
    
def fetch_and_store_saving_products(request):
    # 금융감독원 API URL
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    api_key = "8fbfa11f9a3138d46e386c74e602fbd0"
    topFinGrpNo = "020000"  # 은행 그룹 코드 (시중은행)

    total_data = []  # 데이터를 담을 리스트

    try:
        # 여러 페이지에 걸쳐 데이터를 가져오기
        for page in range(1, 4):  # pageNo를 1부터 3까지 반복
            params = {
                "auth": api_key,
                "topFinGrpNo": topFinGrpNo,
                "pageNo": str(page),
                "numOfRows": "100"  # 100개의 데이터를 가져옵니다
            }
            # API 요청
            response = requests.get(url, params=params)
            data = response.json()

            # 응답 데이터에서 baseList 항목 가져오기
            products = data.get("result", {}).get("baseList", [])
            options = data.get("result", {}).get("optionList", [])
            
            # 데이터를 결합하여 저장
            combined_data = zip(products, options)
            total_data.extend(combined_data)

        # 각 상품 데이터를 데이터베이스에 저장
        for product, option in total_data:
            SavingProduct.objects.create(
                kor_co_nm=product.get("kor_co_nm", ""),
                fin_prdt_nm=product.get("fin_prdt_nm", ""),
                intr_rate_type=option.get("intr_rate_type", ""),
                save_trm=option.get("save_trm", ""),
                intr_rate=float(option.get("intr_rate", 0) or 0),
                intr_rate2=float(option.get("intr_rate2", 0) or 0),
                join_way=product.get("join_way", ""),
                spcl_cnd=product.get("spcl_cnd", ""),
                join_deny=product.get("join_deny", ""),
                join_member=product.get("join_member", ""),
                etc_note=product.get("etc_note", "")
            )

        # 성공 메시지를 템플릿에 전달
        return render(request, 'products/success.html', {'message': '데이터가 성공적으로 저장되었습니다.'})

    except Exception as e:
        # 오류 발생 시 에러 메시지를 템플릿에 전달
        return render(request, 'products/error.html', {'error': str(e)})
