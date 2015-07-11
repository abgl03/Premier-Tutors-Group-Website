from django.shortcuts import render

def index(request):
    return render(request, 'home/PTG_Home.html')