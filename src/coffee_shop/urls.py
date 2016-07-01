from django.conf.urls import url
from django.contrib import admin

from .views import(
    coffee_shop, mailing
)
        
urlpatterns = [
    url(r'^$', coffee_shop),
    url(r'^mailing', mailing),
]
