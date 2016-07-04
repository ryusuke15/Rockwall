from django.conf import settings
from django.contrib import  messages
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import ContactForm, Mailing_listForm
from .models import Blog, Contact, Mailing_list

def coffee_shop(request):
    queryset_list = Blog.objects.order_by("-date")
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
        #Mail Function
        form_email = form.cleaned_data.get("email")
        form_name = form.cleaned_data.get("first_name")+" "+form.cleaned_data.get("last_name")
        form_comment = form.cleaned_data.get("comment")
        
        subject = '1080Brew Contact Form Notification'
        from_email = settings.EMAIL_HOST_USER
        body  = 'Name: %s<br/>Contact: %s<br/>Message: %s<br/>'%(form_name, form_email, form_comment)
        to = 'ryusukelavalla@gmail.com'    
        html_content = body
        text_content = 'This is an example'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        #Message Function
        messages.success(request, "Thank you very much. Your comment has been submitted successfully." )
        return HttpResponseRedirect("/1080_Brew") 

    context={
            "object_list": queryset,
            "title":"1080Brew",
            "form": form
            }
    return render(request,"1080Brew.html", context)



def mailing(request):

    form = Mailing_listForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(request, "Thank you for joining our mailing list." )

        return HttpResponseRedirect("/1080_Brew/mailing")

    context={
            "form": form
            }

    return render(request, "coffee_mailing.html", context)

def test(request):
    return render(request, "coffee.html")

