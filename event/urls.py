from django.urls import path
from event.views import eventForm,search_view,categoryForm,ParticipantForm

urlpatterns = [
    path("eventForm/",eventForm),
    path("categoryForm/",categoryForm, name=""),
    path("participantForm/", ParticipantForm, name=""),
    
    path('search/', search_view, name='search')
    
]
