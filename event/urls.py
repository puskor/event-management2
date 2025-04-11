from django.urls import path
from event.views import eventForm,search_view,categoryForm,ParticipantForm

urlpatterns = [
    path("eventForm/",eventForm,name="eventForm"),
    path("categoryForm/",categoryForm, name="categoryForm"),
    path("participantForm/", ParticipantForm, name="ParticipantForm"),
    
    path('search/', search_view, name='search')
    
]
