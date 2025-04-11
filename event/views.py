from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.forms import Category_form,Event_form,Participant_form
from django.contrib import messages

def categoryForm(request):
    category_form=Category_form()
    if request.method=="POST":
        category_form=Category_form(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"Successfully added")
            return redirect("categoryForm")
            
    context={"category_form":category_form}
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


def ParticipantForm(request):
    category_form=Category_form()
    event_form=Event_form()
    participant_form=Participant_form()
    
    if request.method=="POST":
        participant_form=Participant_form(request.POST)
        if participant_form.is_valid():
            participant_form.save()
            messages.success(request,"SUCCESSFULLY ADDED")
            return redirect("ParticipantForm")
    
    context={"participant_form":participant_form}
    return render(request,"form.html",context)



def search_view(request):
    query = request.GET.get('q', '')
    results = []  # Replace with actual search logic (database query, etc.)
    return render(request, 'search.html', {'query': query, 'results': results})

