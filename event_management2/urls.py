
from django.contrib import admin
from django.urls import path,include
from core.views import base,logged

urlpatterns = [
    path('admin/', admin.site.urls),
    path("event/",include("event.urls")),
    path("user/",include("users.urls")),
    path("",base,name="home"),
    path("logged/",logged,name="logged")
]
