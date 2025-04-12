from django.urls import path
from event.views import eventForm,search_view,categoryForm,participantForm,dashboard,user,update_participant,delete_participant

urlpatterns = [
    path("eventForm/",eventForm,name="eventForm"),
    path("categoryForm/",categoryForm, name="categoryForm"),
    path("participantForm/", participantForm, name="ParticipantForm"),
    path("dashboard/",dashboard),
    path("user/",user,name="user"),
    path("update_participant/<int:id>/",update_participant , name="update_participant"),
    path("delete_participant/<int:id>/",delete_participant, name="delete_participant"),
    
    # path('search/', search_view, name='search')
    
]
