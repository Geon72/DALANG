from django.urls import path
from . import views

urlpatterns = [
    # path('get_bank_savings_products/', views.get_bank_savings_products, name='get_bank_savings_products'),
    path('fetch-deposit-products/', views.fetch_and_store_deposit_products, name='fetch_deposit_products'),
]
