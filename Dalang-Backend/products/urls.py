from django.urls import path
from . import views

urlpatterns = [
    # 초기 상품 데이터 생성하기
    path("get_deposit_products/", views.get_deposit_products),
    path("get_saving_products/", views.get_saving_products),
    # deposit
    path("deposit/", views.deposit_product_list),
    path("deposit/<str:deposit_name>/", views.deposit_detail),
    path("deposit/<str:deposit_name>/option/", views.deposit_option_list),
    path(
        "deposit/<str:deposit_code>/option/<int:option_id>/",
        views.deposit_option_detail,
    ),
    # path('deposit/<str:deposit_code>/interest/', views.deposit_interest),
    path("bank/deposit/<str:bank_name>/", views.bank_deposit),
    # path('deposit/month/<int:month>/', views.deposit_month),
    path("like/deposit/<str:deposit_code>/", views.like_deposit),
    path("recommend/deposit/", views.recommend_deposit_products), # 이미지 배너 추천
    path("filter/deposit/", views.filter_deposit_products), # 예/적금 상품 추천 탭(예금)
    # saving
    path("saving/", views.saving_product_list),
    path("saving/<str:saving_name>/", views.saving_detail),
    path("saving/<str:saving_name>/option/", views.saving_option_list),
    path(
        "saving/<str:saving_code>/option/<int:option_id>/", views.saving_option_detail
    ),
    # path('saving/<str:saving_code>/interest/', views.saving_interest),
    path("bank/saving/<str:bank_name>/", views.bank_saving),
    # path('saving/month/<int:month>/', views.saving_month),
    path("like/saving/<str:saving_code>/", views.like_saving),
    path("recommend/saving/", views.recommend_saving_products),
    path("recommend/saving/second/<str:username>/", views.saving_recommend_second),
]
