from django.urls import path
from . import views

urlpatterns = [
    # path('get_bank_savings_products/', views.get_bank_savings_products, name='get_bank_savings_products'),
    # 정기 예금
    path('fetch_and_store_deposit_products/', views.fetch_and_store_deposit_products, name='fetch_and_store_deposit_products'),
    # 적금
    path('fetch_and_store_saving_products/', views.fetch_and_store_saving_products, name='fetch_and_store_saving_products'),
]
