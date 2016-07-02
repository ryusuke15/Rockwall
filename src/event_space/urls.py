from django.conf.urls import url

from .views import(
    event_home, mailing
)
        
urlpatterns = [
    url(r'^$', event_home),
    url(r'^mailing', mailing),
]
