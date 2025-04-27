
from django.contrib import admin
from django.urls import path,include
from core.views import base,logged,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("event/",include("event.urls")),
    path("users/",include("users.urls")),
    path("",base,name="home"),
    path("logged/",logged,name="logged"),
    path("contact/",contact,name="contact")
]
