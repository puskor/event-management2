from django.shortcuts import render,redirect
from users.forms import Signup_form,Signin_form
from django.contrib import messages
from django.contrib.auth import login,logout



def sign_up(request):
    form=Signup_form()
    if request.method=="POST":
        form=Signup_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get("password1"))
            user.save()
            messages.success(request,"Sign Up successfully")
            return redirect("logged")
        else:
            print("Form is not valid")
    return render(request,"register/sign_up.html",{"form":form})


def sign_in(request):
    form=Signin_form()
    if request.method=="POST":
        form=Signin_form(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("logged")
    return render(request,"register/sign_in.html",{"form":form})
        
def sign_out(request):
    if request.method=="POST":
        logout(request)
        return redirect("home")
    return redirect("home")
        
