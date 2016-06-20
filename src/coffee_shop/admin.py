from django.contrib import admin

# Register your models here.

from .models import Contact, Blog

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email", "received","comment"]
    list_filter = ["received"]
    search_fields = ["email","first_name","last_name", "comment"]
    class Meta:
        model = Contact

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Blog

admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
