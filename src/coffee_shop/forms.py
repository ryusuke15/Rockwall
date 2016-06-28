from django import forms
from .models import Contact, Mailing_list

class ContactForm(forms.ModelForm):
    class Meta:
            model = Contact
            fields = ['first_name','last_name','email','comment']

class Mailing_listForm(forms.ModelForm):
    class Meta:
        model = Mailing_list
        fields = ['email']
