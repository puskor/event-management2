
from django.contrib import admin
from django.urls import path,include
from core.views import base,logged,contact,no_permission

urlpatterns = [
    path('admin/', admin.site.urls),
    path("event/",include("event.urls")),
    path("users/",include("users.urls")),
    path("",base,name="home"),
    path("logged/",logged,name="logged"),
    path("contact/",contact,name="contact"),
    path("no_permission/",no_permission,name="no_permission")
]
 