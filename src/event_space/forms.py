from django import forms
from .models import Contact

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    message = forms.CharField(widget=forms.Textarea)

