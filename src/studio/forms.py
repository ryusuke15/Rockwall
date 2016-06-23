from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker','type':'date'}))
    class Meta:
        model=Contact
        fields = ['first_name', 'last_name', 'email', 'date','message']
