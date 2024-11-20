from django.urls import path
from .views import exchange_rate_view, exchange_rate_chart_view, ExchangeRateListView, ExchangeRateDetailView

urlpatterns = [
    path('exchange_rate_view/', exchange_rate_view, name='exchange_rate_view'),
    path('exchange_rate_chart_view/', exchange_rate_chart_view, name='exchange_rate_chart_view'),
    path('', ExchangeRateListView.as_view(), name='exchange_rate_list'),  # 전체 환율 리스트
    path('detail/', ExchangeRateDetailView.as_view(), name='exchange_rate_detail'),  # 특정 날짜 및 통화 환율 조회
]