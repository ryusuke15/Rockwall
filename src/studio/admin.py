from django.contrib import admin

# Register your models here.
from .models import Contact, Tenant

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email","received"]
    class Meta:
        model = Contact

class TenantAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "room", "email"]
    class Meta:
        model = Tenant

admin.site.register(Contact, ContactAdmin)
admin.site.register(Tenant, TenantAdmin)
