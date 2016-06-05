from django.conf.urls import url

from .views import(
    event_home
)
        
urlpatterns = [
    url(r'^$', event_home),
    # url(r'^submit', submit),
]
