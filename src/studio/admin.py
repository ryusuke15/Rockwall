from django.contrib import admin

# Register your models here.
from .models import Blog, Contact, Mailing_list, Room, Tenant
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","date","spotlight","upcoming","timestamp"]
    list_filter = ["date","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Blog

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","date","email","received"]
    class Meta:
        model = Contact

class Mailing_listAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["email"]
    class Meta:
        model = Mailing_list

class RoomAdmin(admin.ModelAdmin):
    list_display = ["room", "size", "rent"]
    list_filter = ["size","rent"]
    search_fields = ["room","size","rent"]
    class Meta:
        model = Room

class TenantAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "room", "email"]
    class Meta:
        model = Tenant

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Mailing_list, Mailing_listAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Tenant, TenantAdmin)
