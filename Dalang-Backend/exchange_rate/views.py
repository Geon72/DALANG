from django.shortcuts import render

def exchange_rate(request):
    return render(request, 'exchange_rate/exchange_rate.html')