from django.shortcuts import render

# Create your views here.
def kakaomap(request):
    return render(request, 'kakaomap/kakaomap.html')