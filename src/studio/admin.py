# from djangoseo.admin import register_seo_admin
from django.contrib import admin
# from mysite.seo import MyMetadata
from .forms import BlogForm
from image_cropping import ImageCroppingMixin

# Register your models here.
from .models import Blog, Contact, Coworking_Space,Mailing_list, Room, Tenant

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","date","spotlight","timestamp","admin_image"]
    list_filter = ["date","timestamp"]
    search_fields = ["title","content"]
    form = BlogForm

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","date","email","received"]
    class Meta:
        model = Contact


class CoworkAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email","received"]
    class Meta:
        model = Coworking_Space

class Mailing_listAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["email"]
    class Meta:
        model = Mailing_list

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ["room", "size", "rent"]
#     list_filter = ["size","rent"]
#     search_fields = ["room","size","rent"]
#     class Meta:
#         model = Room

class TenantAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "room", "email"]
    class Meta:
        model = Tenant


# register_seo_admin(admin.site, MyMetadata)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Coworking_Space, CoworkAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Mailing_list, Mailing_listAdmin)
# admin.site.register(Room, RoomAdmin)
admin.site.register(Tenant, TenantAdmin)
