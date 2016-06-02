from django.conf.urls import url
from django.contrib import admin

from .views import(
    home, studio, directory,
)
        
urlpatterns = [
    url(r'^$', home),
    url(r'^studio', studio),
    url(r'^directory', directory)
    # url(r'^submit', submit),
]
