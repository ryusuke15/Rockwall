from django.contrib import admin
from models import Blog, Contact
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "time","recent", "upcoming", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Blog

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "email","received"]
    class Meta:
        model = Contact
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)

