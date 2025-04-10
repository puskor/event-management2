from django.shortcuts import render
from django.http import HttpResponse
from event.forms import Category_form,Event_form,Participant_form

def categoryForm(request):
    category_form=Category_form
    context={"category_form":category_form}
    return render(request,"form.html",context)



def eventForm(request):
    category_form=Category_form
    event_form=Event_form
    context={"category_form":category_form,"event_form":event_form}
    return render(request,"form.html",context)


def ParticipantForm(request):
    category_form=Category_form
    event_form=Event_form
    participant_form=Participant_form
    context={"category_form":category_form,"event_form":event_form,"participant_form":participant_form}
    return render(request,"form.html",context)



def search_view(request):
    query = request.GET.get('q', '')
    results = []  # Replace with actual search logic (database query, etc.)
    return render(request, 'search.html', {'query': query, 'results': results})

