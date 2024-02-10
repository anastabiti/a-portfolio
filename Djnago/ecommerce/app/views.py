from django.http import HttpResponse
# create a user
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect


def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('/auth')



def create_user(request):
    if(request.method == 'POST'):
            role  =request.POST.get("role")
            if(role == "client"):
                group = Group.objects.get(name="buyers")
                user =User.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
                user.groups.add(group)
                user.save()
                return HttpResponse(user.groups.all())
            if(role == "seller"):
                group = Group.objects.get(name="sellers")
                user =User.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
                user.groups.add(group)
                user.save()
                return HttpResponse(user.groups.all())
            else:
                return HttpResponse("no such role")
                 
    return HttpResponse(request.POST)
def login_(request):
        print(request.method , " method")
        if(request.method == "POST"):
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            # return None if the auth failed
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("NOT LOGGED")
        if(request.method == "DELETE"):
            print("logout is called !!!+!+!+!+!+!+!++!")
            logout(request)
            return HttpResponse("logout is done")
        if(request.method == "GET"):
            return render(request, 'login.html')
def logout_(request):
        print(request.method , " method")
        if(request.method == "POST"):
            print("logout is called !!!+!+!+!+!+!+!++!")
            logout(request)
            return HttpResponse("logout is done")

