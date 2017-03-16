from django.conf.urls import url
from django.contrib import admin

from .views import(
    home, studio, directory, contact, coworking,available, tour, floorplan, mailing
)
        
urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^studio', studio, name="studio"),
    url(r'^co_working_space', coworking, name="coworking"),
    url(r'^contact', contact, name="contact"),
    url(r'^tour', tour, name="tour"),
    url(r'^mailing', mailing, name="mail")
]
