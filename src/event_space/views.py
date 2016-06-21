from django.contrib import  messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Blog
from .forms import ContactForm

# Create your views here.

def event_home(request):
    queryset_list = Blog.objects.order_by("-date").filter(recent=False, upcoming=False)
    
    recent = Blog.objects.order_by("-date").filter(recent=True)    
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
   
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you very much. Your comment has been submitted successfully." )
        return HttpResponseRedirect("/event_space") 

    context={
            "object_list": queryset,
            "form":form,
            "recent": recent,
            "upcoming": upcoming
            }
   
    return render(request,"event_home.html", context)

