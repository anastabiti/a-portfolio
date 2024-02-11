from django.http import HttpResponse
# create a user
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect



# My Models 
from app.models import Products
def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('/auth')



def create_user(request):
    if(request.method == 'POST'):
        # try:
            role  =request.POST.get("role")
            if(role == "seller"):
                group = Group.objects.get(name="sellers")
                user =User.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
                user.groups.add(group)
                user.save()
                login(request,user)
                return redirect('/')

            else:
                return HttpResponse("no such role")
        # except:
        #     return HttpResponse("An exception occurred", status=400)
        
    if(request.method == 'GET'):  
        return render(request, 'signup_seller.html')
    

def create_user_buyer(request):
    if(request.method == 'POST'):
            role  =request.POST.get("role")
            if(role == "client"):
                group = Group.objects.get(name="buyers")
                user =User.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
                user.groups.add(group)
                user.save()
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("no such role")
    if(request.method == 'GET'):  
        return render(request, 'signup_buyer.html')

                 
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
                return HttpResponse('Not logged', status=401)
        if(request.method == "DELETE"):
            print("logout is called !!!+!+!+!+!+!+!++!")
            logout(request)
            return redirect('/')
        if(request.method == "GET"):
            return render(request, 'login.html')
def logout_(request):
        print(request.method , " method")
        if(request.method == "POST"):
            print("logout is called !!!+!+!+!+!+!+!++!")
            logout(request)
            return redirect('/')

def list_product(request):
    user=  request.user
    if(request.user.is_authenticated):
        if(request.method == "POST"):
            if user.groups.filter(name = "sellers").exists():
                name  =request.POST.get("name")
                price  =request.POST.get("price")
                new_product = Products(name=name, price=price, seller=user)
                new_product.save()
                return  HttpResponse("DONE : created")
        if((request.method == "GET") and (user.groups.filter(name = "sellers").exists())):
            return render(request, 'list_product.html')
        
    return HttpResponse('NOT a seller / Not logged', status=401)
    