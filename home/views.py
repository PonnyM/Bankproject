# from django.shortcuts import render
# import requests
# def home(request):
#     return render(request,'home/home.html')

# Create your views here.

from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
