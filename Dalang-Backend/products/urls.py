from django.urls import path
from .views import (
    fetch_and_store_deposit_products,
    fetch_and_store_saving_products,
    DepositProductListView,
    DepositProductDetailView,
    SavingProductListView,
    SavingProductDetailView,
    RecommendProductsView,
)

urlpatterns = [
    # 정기 예금 -> 20241120 2055 DB 저장 완료
    path('fetch_and_store_deposit_products/', fetch_and_store_deposit_products, name='fetch_and_store_deposit_products'),
    # 적금 -> 20241120 2055 DB 저장 완료
    path('fetch_and_store_saving_products/', fetch_and_store_saving_products, name='fetch_and_store_saving_products'),
    path('deposit-products/', DepositProductListView.as_view(), name='deposit_product_list'),  # 정기 예금 전체 조회
    path('deposit-products/<int:pk>/', DepositProductDetailView.as_view(), name='deposit_product_detail'),  # 특정 정기 예금 조회
    path('saving-products/', SavingProductListView.as_view(), name='saving_product_list'),  # 적금 전체 조회
    path('saving-products/<int:pk>/', SavingProductDetailView.as_view(), name='saving_product_detail'),  # 특정 적금 조회
    path('recommend-products/', RecommendProductsView.as_view(), name='recommend_products'), # 유저 정보에 적합한 상품 추천 -> 어떻게 해야 할까...
]
