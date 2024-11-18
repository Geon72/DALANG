# import requests
# from django.shortcuts import render
# 
# def get_bank_savings_products(request):
#     # 금융감독원 API URL
#     url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'  # 실제 API URL로 대체하세요

#     # API 키를 포함한 요청 파라미터 설정
#     params = {
#         "auth": "8fbfa11f9a3138d46e386c74e602fbd0",  # 발급받은 API 키를 입력하세요
#         "topFinGrpNo": "020000",  # 은행 그룹 코드 (예: 은행 코드)
#         "pageNo": "1",            # 페이지 번호
#         "numOfRows": "10"         # 페이지당 데이터 개수
#     }

#     try:
#         # API 요청
#         response = requests.get(url, params=params)
#         data = response.json()  # 응답 데이터를 JSON으로 파싱

#         # 응답 데이터에서 예적금 상품 정보를 가져옵니다
#         # 응답 데이터에서 baseList 항목을 가져옵니다
#         products = data.get("result", {}).get("baseList", [])
#         options = data.get("result", {}).get("optionList", [])
        
#         combined_data = zip(products, options)

#         # 템플릿에 데이터 전달
#         return render(request, 'deposits/bank_products.html', {'combined_data': combined_data})

#     except Exception as e:
#         # 오류 발생 시 에러 메시지를 템플릿에 전달
#         return render(request, 'deposits/bank_products.html', {'error': str(e)})

# 시중은행 예금 상품 데이터 from 금융감독원 정기예금 API
import requests
from django.shortcuts import render
from .models import DepositProduct

def fetch_and_store_deposit_products(request):
    # 금융감독원 API URL
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

    # API 키를 포함한 요청 파라미터 설정
    params = {
        "auth": "8fbfa11f9a3138d46e386c74e602fbd0",
        "topFinGrpNo": "020000",  # 은행 그룹 코드 (시중은행)
        "pageNo": "1",
        "numOfRows": "100"  # 100개의 데이터를 가져옵니다
    }

    try:
        # API 요청
        response = requests.get(url, params=params)
        data = response.json()

        # 응답 데이터에서 baseList 항목 가져오기
        products = data.get("result", {}).get("baseList", [])
        options = data.get("result", {}).get("optionList", [])
        
        combined_data = zip(products, options)

        # 각 상품 데이터를 데이터베이스에 저장
        for product, option in combined_data:
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
        return render(request, 'deposits/success.html', {'message': '데이터가 성공적으로 저장되었습니다.'})

    except Exception as e:
        # 오류 발생 시 에러 메시지를 템플릿에 전달
        return render(request, 'deposits/error.html', {'error': str(e)})
