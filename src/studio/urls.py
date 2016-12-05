from django.conf.urls import url
from django.contrib import admin

from .views import(
    home, studio, directory, contact, coworking,available, tour, floorplan, mailing
)
        
urlpatterns = [
    url(r'^$', home),
    url(r'^studio', studio),
    url(r'^co_working_space', coworking),
    url(r'^contact', contact),
    # url(r'^directory', directory),
    # url(r'^directory', directory),
    # url(r'^available_spaces', available), 
    url(r'^tour', tour),
    # url(r'^floorplan', floorplan),
    url(r'^mailing', mailing)
]
