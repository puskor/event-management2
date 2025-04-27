from django.shortcuts import render,redirect
from users.forms import Signup_form,Signin_form,Assign_roll_form,Create_group_form
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from django.db.models import Prefetch



def sign_up(request):
    form=Signup_form()
    if request.method=="POST":
        form=Signup_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get("password1"))
            user.is_active=False
            user.save()
            messages.success(request,"Please check your mail")
            return redirect("sign_in")
        else:
            print("Form is not valid")
    return render(request,"register/sign_up.html",{"form":form})


def sign_in(request):
    form=Signin_form()
    if request.method=="POST":
        form=Signin_form(data=request.POST)
        print("post method par hoice")
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            print("finali acce")
            return redirect("logged")
        else:
            print(form.errors)
            print("error")
    print("sign in kaj kore nai")
    return render(request,"register/sign_in.html",{"form":form})
        
def sign_out(request):
    if request.method=="POST":
        logout(request)
        return redirect("home")
    return redirect("home")
        

def activate_user(request,user_id,token):
    try:
        user=User.objects.get(id=user_id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,"Please check your mail")
            return redirect("sign_in")
        else:
            return HttpResponse("Invalid token or user id")
            
    except User.DoesNotExist:
        return HttpResponse('User not found')
    
    

def admin_dashboard(request):
    users=User.objects.prefetch_related(
        Prefetch("groups",queryset=Group.objects.all(),to_attr="all_groups")
    ).all()
    for user in users:
        if user.all_groups:
            user.group_name=user.all_groups[0].name
        else:
            user.group_name="No group assign"
    return render(request,"admin/dashboard.html",{"users":users})

def assign_roll(request,user_id):
    user=User.objects.get(id=user_id)
    form=Assign_roll_form()
    if request.method=="POST":
        form=Assign_roll_form(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get("role")
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin_dashboard')
    return render(request,"admin/assign_roll.html",{"form":form})


def create_group(request):
    form=Create_group_form()
    if request.method=="POST":
        form=Create_group_form(request.POST)
        if form.is_valid():
            group=form.save()
            messages.success(request,f"{group.name} group create successfully")
            return redirect("admin_dashboard")
    return render(request,"admin/create_group.html",{"form":form})

def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'admin/group_list.html', {'groups': groups})

