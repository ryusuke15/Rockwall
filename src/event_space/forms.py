from pagedown.widgets import AdminPagedownWidget
from django import forms
from .models import Blog, Contact, Mailing_list

class BlogForm(forms.ModelForm):
   content = forms.CharField(widget=AdminPagedownWidget())     
   class Meta:
        model = Blog
        fields = '__all__'

class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker','type':'date'}))
    class Meta:
        model=Contact
        fields = ['first_name', 'last_name', 'email', 'date','message']

class Mailing_listForm(forms.ModelForm):
    class Meta:
        model = Mailing_list
        fields = ['email']
