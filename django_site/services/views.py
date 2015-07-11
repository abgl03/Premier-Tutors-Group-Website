from django.shortcuts import render

def index(request):
    return render(request, 'services/PTG_Services.html')