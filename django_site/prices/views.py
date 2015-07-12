from django.shortcuts import render

def index(request):
    return render(request, 'prices/PTG_Prices.html')