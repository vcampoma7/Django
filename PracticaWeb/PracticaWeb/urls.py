from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^flylo/', include('flylo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^flylo/', include('flylo.urls',namespace='flylo')),
]
