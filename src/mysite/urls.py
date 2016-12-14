from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include("studio.urls")),
    url(r'^1080_Brew/', include("coffee_shop.urls")),
    url(r'^project_space/', include("event_space.urls")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]
# if settings.DEBUG:
#     urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
