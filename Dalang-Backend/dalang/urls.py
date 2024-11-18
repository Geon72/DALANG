from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposits/', include('deposits.urls')),
    path('kakaomap/', include('kakaomap.urls')),
    path('exchange_rate/', include('exchange_rate.urls')),
]
