from django.urls import path
from event.views import eventForm,categoryForm,participantForm,dashboard,user,update_participant,delete_participant,update_event,update_category,delete_category,delete_event

urlpatterns = [
    path("eventForm/",eventForm,name="eventForm"),
    path("categoryForm/",categoryForm, name="categoryForm"),
    path("participantForm/", participantForm, name="ParticipantForm"),
    path("dashboard/",dashboard),
    path("user/",user,name="user"),
    
    path("update_participant/<int:id>/",update_participant , name="update_participant"),
    path("update_event/<int:id>/",update_event,name="update_event"),
    path("update_category/<int:id>/",update_category,name="update_category"),
    
    path("delete_participant/<int:id>/",delete_participant, name="delete_participant"),
    path("delete_event/<int:id>/",delete_event,name="delete_event"),
    path("delete_category/<int:id>/",delete_category,name="delete_category"),
    
    # path('search/', search_view, name='search')
    
]
