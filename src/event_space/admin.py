from django.contrib import admin
from models import Blog, Contact, Mailing_list
from .forms import BlogForm

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "time","recent", "upcoming", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title","content"]
    form = BlogForm
class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "email","received"]
    class Meta:
        model = Contact

class Mailing_listAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["email"]

#admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Mailing_list, Mailing_listAdmin)
