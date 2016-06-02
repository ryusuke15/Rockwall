from django.contrib import admin
from models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "date", "time", "received"]
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)

