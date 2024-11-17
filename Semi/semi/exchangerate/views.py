from django.shortcuts import render

def exchangerate(request):
    return render(request, 'exchangerate/exchangerate.html')