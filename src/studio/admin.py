from django.contrib import admin

# Register your models here.
from .models import Blog, Contact, Tenant
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","date","spotlight","upcoming","timestamp"]
    list_filter = ["date","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Blog

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email","received"]
    class Meta:
        model = Contact

class TenantAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "room", "email"]
    class Meta:
        model = Tenant

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tenant, TenantAdmin)
