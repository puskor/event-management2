from django.urls import path
from event.views import hello,test,search_view

urlpatterns = [
    path("hello/",hello),
    path("test/",test),
    
    path('search/', search_view, name='search')
    
]
