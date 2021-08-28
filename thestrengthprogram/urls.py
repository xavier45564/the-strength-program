from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('appointments/', appointment, name="appointment"),
    path('resume/', contact, name="contact"),
    path('services/', services, name="services"),
    path('team-details/', teamDetails, name="team-details"),
    path('team/', team, name="team"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()