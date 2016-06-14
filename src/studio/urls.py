from django.conf.urls import url
from django.contrib import admin

from .views import(
    home, studio, directory, available, tour, floorplan
)
        
urlpatterns = [
    url(r'^$', home),
    url(r'^studio', studio),
    url(r'^directory', directory),
    url(r'^available_spaces', available), 
    url(r'^tour', tour),
    url(r'^floorplan', floorplan)
    
    # url(r'^submit', submit),
]
