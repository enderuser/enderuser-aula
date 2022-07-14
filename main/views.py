from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home_main.html')

def contact(request):
    return render(request, 'contact_main.html')
