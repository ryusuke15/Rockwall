from django.contrib import admin

# Register your models here.

from .models import Contact, Blog, Mailing_list

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email", "received","comment"]
    list_filter = ["received"]
    search_fields = ["email","first_name","last_name", "comment"]
    class Meta:
        model = Contact

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","date","timestamp"]
    list_filter = ["timestamp","date"]
    search_fields = ["title","content"]
    class Meta:
        model = Blog

class Mailing_listAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["email"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Mailing_list, Mailing_listAdmin)
