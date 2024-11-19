from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('products/', include('products.urls')),
    path('articles/', include('articles.urls')),
    path('kakaomap/', include('kakaomap.urls')),
    path('exchange_rate/', include('exchange_rate.urls')),
]