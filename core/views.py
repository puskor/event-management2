from django.shortcuts import render,redirect


def base(request):
    return render(request,"base.html")

def logged(request):
    return render(request,"logged.html")

def home_page(request):
    return render(request,"home.html")


def contact(request):
    return render(request,"contact.html")

def no_permission(request):
    return render(request,"no_permission.html")