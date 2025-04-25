from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.forms import Category_form,Event_form,Participant_form
from django.contrib import messages
from event.models import Event,Category,Participant
from django.db.models import Count
def categoryForm(request):
    category_form=Category_form()
    if request.method=="POST":
        category_form=Category_form(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"Successfully added")
            return redirect("categoryForm")
            
    context={"category_form":category_form }
    return render(request,"form.html",context)


def eventForm(request):
    category_form=Category_form()
    event_form=Event_form()
    if request.method=="POST":
        event_form=Event_form(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Successfully added")
            return redirect("eventForm")
    context={"event_form":event_form}
    return render(request,"form.html",context)


def participantForm(request):
    participant_form=Participant_form()
    
    if request.method=="POST":
        participant_form=Participant_form(request.POST)
        if participant_form.is_valid():
            participant_form.save()
            messages.success(request,"SUCCESSFULLY ADDED")
            return redirect("ParticipantForm")
    
    context={"participant_form":participant_form}
    return render(request,"form.html",context)


def dashboard(request):
    return render(request,"dashboard/navbar.html")

def user(request):
    show_event=request.GET.get("show")=="event"
    events = Event.objects.all() if show_event else []
    
        
    show_participant = request.GET.get("show") == "participant"
    participants = Participant.objects.prefetch_related("event").all() if show_participant else []
    
    show_category=request.GET.get("show")=="category"
    categorys = Category.objects.all() if show_category else []
    
    
    
    event_counts=Event.objects.aggregate(
        total=Count("id")
    )
    category_counts=Category.objects.aggregate(
        total=Count("id")
    )
    participant_counts=Participant.objects.aggregate(
        total=Count("id")
    )

    context = {
        "events": events,
        "categorys": categorys,
        "participants":participants,
        "event_counts":event_counts,
        "category_counts":category_counts,
        "participant_counts":participant_counts
        
    }
    return render(request, "dashboard/user.html", context)


def update_participant(request, id):
    participant = Participant.objects.get(id=id)
    
    if request.method == "POST":
        participant_form = Participant_form(request.POST, instance=participant)
        if participant_form.is_valid():
            participant_form.save()
            messages.success(request, "SUCCESSFULLY UPDATED")
            return redirect("ParticipantForm")
    else:
        participant_form = Participant_form(instance=participant)
    
    context = {"participant_form": participant_form}
    return render(request, "form.html", context)

def delete_participant(request,id):
    if request.method=="POST":
        participant=Participant.objects.get(id=id)
        participant.delete()
        messages.success(request,"Delete successfully")
    else:
        messages.error(request,"Something is wrong")
        
    return redirect("user")
    

def update_event(request,id):
    event=Event.objects.get(id=id)
    
    if request.method=="POST":
        event_form=Event_form(request.POST ,instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"SUCCESSFULLY UPDATED")
            return redirect("eventForm")
    else:
        event_form=Event_form(instance=event)
        
    context={"event_form":event_form}
    return render(request,"form.html",context)
    

def delete_event(request,id):
    if request.method=="POST":
        event=Event.objects.get(id=id)
        event.delete()
        messages.success(request,"SUCCESSFULLY DELETE")
    else:
        messages.error(request,"Something WRONG")
        
    return redirect("user")

def update_category(request,id):
    category=Category.objects.get(id=id)
    if request.method=="POST":
        category_form=Category_form(request.POST ,instance=category)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"SUCCESSFULLY UPDATE")
    else:
        category_form=Category_form(instance=category)
        
    context={"category_form":category_form}
    return render(request,"form.html",context)

def delete_category(request,id):
    if request.method=="POST":
        category=Category.objects.get(id=id)
        category.delete()
        messages.success(request,"SUCCESSFULLY DELETE")
        
    else:
        messages.error(request,"Something WRONG")
    
    return redirect("user")



def navbar(request):
    return render(request,"dashboard/navbar.html")






