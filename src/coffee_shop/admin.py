from django.contrib import admin

# Register your models here.

from .models import Mailing_List

class Mailing_ListModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","received"]
    
    class Meta:
        model = Mailing_List

admin.site.register(Mailing_List, Mailing_ListModelAdmin)
