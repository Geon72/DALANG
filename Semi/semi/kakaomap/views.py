from django.shortcuts import render

def kakaomap(request):
    return render(request, 'kakaomap/kakaomap.html')