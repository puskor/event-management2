from django.urls import path
from event.views import hello

urlpatterns = [
    path("hello/",hello)
]
