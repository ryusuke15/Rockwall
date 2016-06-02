from django.http import HttpResponse
from django.shortcuts import render

from .models import Tenant
# Create your views here.

def home(request):
    return render(request,"home.html")

def directory(request):
    return render(request,"directory.html")

def studio(request):
    return render(request,"studio.html")


