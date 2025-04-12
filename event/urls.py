from django.urls import path
from event.views import eventForm,search_view,categoryForm,participantForm,dashboard,user

urlpatterns = [
    path("eventForm/",eventForm,name="eventForm"),
    path("categoryForm/",categoryForm, name="categoryForm"),
    path("participantForm/", participantForm, name="ParticipantForm"),
    path("dashboard/",dashboard),
    path("user/",user),
    
    # path('search/', search_view, name='search')
    
]
