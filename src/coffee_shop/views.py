from django.shortcuts import render

# Create your views here.
from .forms import ContactForm
from .models import Mailing_List

def coffee_shop(request):

    form = ContactForm(request.POST or None);
    if form.is_valid():
        form_email = form.cleaned_data.get("email")

    instance = form.save(commit=False)
    instance.save()
    
    context={
            "form": form
            }

    return render(request,"1080Brew.html", context)


