from django.contrib import  messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render

from .models import Blog, Tenant
from .forms import ContactForm
# Create your views here.
def home(request):
    queryset_list = Blog.objects.order_by("-date").filter(spotlight=False, upcoming=False)
    
    spotlight = Blog.objects.order_by("-date").filter(spotlight=True)    
    upcoming = Blog.objects.order_by("-date").filter(upcoming = True)

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    context={
            "object_list": queryset,
            "spotlight": spotlight,
            "upcoming": upcoming
            }
    return render(request,"home.html", context)


def directory(request):
    queryset_list = Tenant.objects.order_by("last_name")
    query = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |        
            Q(content__icontains=query) |
            Q(room__icontains=query) |
            Q(email__icontains=query)|
            Q(web__icontains=query)
            ).distinct()
    
    paginator = Paginator(queryset_list, 10)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
		"object_list": queryset, 
    }
    return render(request,"directory.html", context)

def studio(request):
    return render(request,"studio.html")

def available(request):
    return render(request,"available_spaces.html")

def tour(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():

        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you very much. Your request has been submitted successfully." )
        return HttpResponseRedirect("/tour") 


    context={
            "form":form,
            }

    return render(request,"tour.html", context)




def floorplan(request):
    return render(request,"floorplan.html")

