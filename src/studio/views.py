from django.conf import settings
from django.contrib import  messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm, Mailing_listForm 
from .models import Blog, Room, Tenant
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
    queryset = Room.objects.order_by("room")

    context = {
		"object_list": queryset, 
    }

    return render(request,"available_spaces.html", context)

def tour(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        form_email = form.cleaned_data.get("email")
        form_name = form.cleaned_data.get("first_name")+" "+form.cleaned_data.get("last_name")
        form_message = form.cleaned_data.get("message")
        form_date = form.cleaned_data.get("date")

        subject = 'Tour Contact Form Notification'
        from_email = settings.EMAIL_HOST_USER
        body  = 'Name: %s<br/>Contact: %s<br/>Request Date: %s<br/>Message: %s<br/>'%(form_name, form_email, form_date, form_message)
        to = 'Reception@Rockwallstudios.nyc'    
        html_content = body
        text_content = 'This is an example'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, "Thank you very much. Your request has been submitted successfully." )
        return HttpResponseRedirect("/tour") 


    context={
            "form":form,
            }

    return render(request,"tour.html", context)

def mailing(request):
    form = Mailing_listForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        form_email = form.cleaned_data.get("email")
        
        subject = 'Studios Email Form Notification'
        from_email = settings.EMAIL_HOST_USER
        body  = 'Please add %s to the mailing list.'%(form_email)
        to = 'Reception@Rockwallstudios.nyc'    
        html_content = body
        text_content = 'This is an example'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        messages.success(request, "Thank you for joining our mailing list." )

        return HttpResponseRedirect("/mailing")

    context={
            "form": form
            }

    return render(request, "studio_mailing.html", context)
   


def floorplan(request):
    return render(request,"floorplan.html")

