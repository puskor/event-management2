from django.shortcuts import render
from django.http import HttpResponse



def hello(request):
    return HttpResponse("hello boyes")

def test(request):
    return render(request,"test.html")

def search_view(request):
    query = request.GET.get('q', '')
    results = []  # Replace with actual search logic (database query, etc.)
    return render(request, 'search.html', {'query': query, 'results': results})

