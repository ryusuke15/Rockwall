from django.conf import settings
from django.contrib import  messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Blog, Contact
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

        form_email = form.cleaned_data.get("email")
        form_name = form.cleaned_data.get("first_name")+" "+form.cleaned_data.get("last_name")
        form_message = form.cleaned_data.get("message")
        form_date = form.cleaned_data.get("date")

        subject = 'Project Space Contact Form Notification'
        from_email = settings.EMAIL_HOST_USER
        body  = 'Name: %s<br/>Contact: %s<br/>Request Date: %s<br/>Message: %s<br/>'%(form_name, form_email, form_date, form_message)
        to = 'ryusukelavalla@gmail.com'    
        html_content = body
        text_content = 'This is an example'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, "Thank you very much. Your request has been submitted successfully." )
        return HttpResponseRedirect("/project_space") 

    context={
            "object_list": queryset,
            "form":form,
            "recent": recent,
            "upcoming": upcoming
            }
   
    return render(request,"event_home.html", context)

