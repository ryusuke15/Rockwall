from django import forms
from .models import Contact, Coworking_Space, Mailing_list

class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker','type':'date'}))
    class Meta:
        model=Contact
        fields = ['first_name', 'last_name', 'email', 'date','message']

class Coworking_SpaceForm(forms.ModelForm):
    class Meta:
        model=Coworking_Space
        fields = ['first_name', 'last_name', 'email', 'message']

class Mailing_listForm(forms.ModelForm):
    class Meta:
        model = Mailing_list
        fields = ['email']
