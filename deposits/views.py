from django.shortcuts import render
from django.http import HttpResponse
import requests

def display(request):
    url = "http://www.datacamp.com"
    url_check = requests.get(url,verify=False)
    return HttpResponse(f"The status code of the {url} is {url_check.status_code}")
def index(request):
    # return HttpResponse("INDEX VIEW IS WORKING")
    return render(request,'deposits/base.html')

#     return render(request,'deposits/base.html')
# Create your views here.
