from django.shortcuts import render

# Create your views here.

def event_home(request):

    return render(request,"event_home.html")
