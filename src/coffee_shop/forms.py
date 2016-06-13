from django import forms
from .models import Mailing_List

class ContactForm(forms.ModelForm):
    class Meta:
            model = Mailing_List
            fields = ['email']
