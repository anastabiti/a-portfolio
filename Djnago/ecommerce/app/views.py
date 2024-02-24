import base64
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.http import HttpResponse, JsonResponse
# create a user
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from imagekitio import ImageKit
from .models import MyUser
import environ
import requests
import stripe
env = environ.Env()
from django.core.validators import validate_email #https://docs.djangoproject.com/en/3.0/ref/forms/validation/



# My Models 
from app.models import Products
def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('/auth')



def create_user(request):
    if(request.method == 'POST'):
        try:
            role  =request.POST.get("role")
            if(role == "seller"):
                existing_group = Group.objects.filter(name="sellers").first()
                if not existing_group:
                    Group.objects.create(name='sellers')
                group = Group.objects.get(name="sellers")
                print("group ", group)
                email = request.POST.get("email")
                username = request.POST.get('username') 
                password = request.POST.get("password")
                if(email and username and password is not None):
                    username_validator = UnicodeUsernameValidator()
                    username_validator(username)
                    validate_email(email)
                    user =MyUser.objects.create_user(username,email,password)
                    user.groups.add(group)
                    user.save()
                    print(user.groups)
                    login(request,user)
                    return redirect('/')
                else:
                    return HttpResponse("password/username/email are empty", status=400)
        except Exception as e:
            error_message = str(e) 
            return HttpResponse(error_message, status=400)
    if(request.method == 'GET'):  
        return render(request, 'signup_seller.html')
    

def create_user_buyer(request):
    if(request.method == 'POST'):
        try:
            role  =request.POST.get("role")
            if(role == "client"):
                existing_group = Group.objects.filter(name="buyers").first()
                if not existing_group:
                    Group.objects.create(name='buyers')
                group = Group.objects.get(name="sellers")
                print("group ", group)
                email = request.POST.get("email")
                username = request.POST.get('username') 
                password = request.POST.get("password")
                if(email and username and password is not None):
                    username_validator = UnicodeUsernameValidator()
                    username_validator(username)
                    validate_email(email)
                    user =MyUser.objects.create_user(username,email,password)
                    user.groups.add(group)
                    user.save()
                    print(user.groups)
                    login(request,user)
                    return redirect('/')
                else:
                    return HttpResponse("password/username/email are empty", status=400)
        except Exception as e:
            error_message = str(e) 
            return HttpResponse(error_message, status=400)
    if(request.method == 'GET'):  
        return render(request, 'signup_buyer.html')
    


# def create_user_buyer(request):
#     if(request.method == 'POST'):
#             role  =request.POST.get("role")
#             if(role == "client"):
#                 group = Group.objects.get(name="buyers")
#                 user =MyUser.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
#                 user.groups.add(group)
#                 user.save()
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 return HttpResponse("no such role")
#     if(request.method == 'GET'):  
#         return render(request, 'signup_buyer.html')

                 
    return HttpResponse(request.POST)
def login_(request):
        try:
            if(request.method == "POST"):
                email_ = request.POST.get("email")
                password_ = request.POST.get("password")
                validate_email(email_)
                if(email_ and password_ is not None):
                    user = authenticate(username=email_, password=password_)
                    # return None if the auth failed
                    if user is not None:
                        login(request,user)
                        return redirect('/')
                raise Exception('ERROR')
            if(request.method == "GET"):
                return render(request, 'login.html')
        except Exception as e:
            error_message = str(e) 
            return HttpResponse(error_message, status=400)        


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
                stripe.api_key = env("STRIPESECRETKEY")
                product = stripe.Product.create(name=name)
                price_strip = stripe.Price.create(product=product.id,unit_amount=price, currency='usd')
                print(product.id , " product hna")
                print(price_strip.id , " price hna")
                new_product.Price_ID = price_strip.id
                new_product.save()
                return  HttpResponse("DONE : created")
        if((request.method == "GET") and (user.groups.filter(name = "sellers").exists())):
            return render(request, 'list_product.html')
        
    return HttpResponse('NOT a seller / Not logged', status=401)

def all_products(request):
    # fruits = Fruit.objects.all()
    # render(request, 'index.html', {'fruits': fruits})
    user=  request.user
    if(user.is_authenticated):
        products = Products.objects.values()
        # return render(request, 'list_product.html', {'products': products})
        # return JsonResponse({'products': list(products)})
        return render(request,'buy.html')
    return redirect('/')
def get_all_products(request):
    user=  request.user
    if(user.is_authenticated):
        products = Products.objects.values()
        return JsonResponse({'products': list(products)})
    return redirect('/')



def get_all_user(request):
    user=  request.user
    if(user.is_authenticated):
        # users  = User.objects.values_list()
        users = MyUser.objects.values('id', 'username', 'email')  
        return JsonResponse({'users':list(users)})


def uploading(request):
        if(request.user.is_authenticated):
            if(request.method == "POST"):
                file_ = request.FILES["image"]
                file_content = file_.read()
                # print(file_content)

                image_ =ImageKit(
                    private_key=env("private_key"),
                    public_key=env("public_key"),
                    url_endpoint=env("url_endpoint"),
                    )
                file_content_base64 = base64.b64encode(file_content).decode('utf-8')

                url = image_.upload(
                file=file_content_base64,
                file_name=file_.name,
                )                
                request.user.image = url.url
                request.user.save()
                return HttpResponse("done")
        return HttpResponse("Not logged")



def google_auth(request):
    return redirect(f'https://accounts.google.com/o/oauth2/v2/auth?client_id={env("client_id")}&redirect_uri=http://localhost:8000/google/callback&response_type=code&scope=email%20profile')

def google_auth_callback(request):
    # try:
        # redirect()
        code = request.GET.get('code')
        print(code , "  {code}")
        data = {
        'code': code, 
        'client_id': env("client_id"),
        'client_secret': env("client_secret"),
        'redirect_uri': 'http://localhost:8000/google/callback',
        'grant_type': 'authorization_code'
    }

        res =requests.post('https://oauth2.googleapis.com/token',data=data)
        if(res is not None):
        #     # print(res.json()['access_token'])
        #     return HttpResponse(res.json()['access_token'])
            access_token =res.json()['access_token']
            if(access_token is not None):
                headers = {'Authorization': f'Bearer {access_token}'}
                profile =requests.post("https://www.googleapis.com/oauth2/v3/userinfo", headers=headers)
                print(profile.json())
                try:
                    user = MyUser.objects.get(email__exact=profile.json()['email'])
                    if(user is not None):
                        login(request,user)
                        return redirect("/")
                except:
                    print("NO such user")
                    existing_group = Group.objects.filter(name="buyers").first()
                    if not existing_group:
                        Group.objects.create(name='buyers')
                    group = Group.objects.get(name="buyers")
                    username__ = profile.json()['name']
                    email__ =profile.json()['email']
                    # password__ = "22222" # c=must be changed
                    # print(username__, email__, password__ , " +++++")
                    new_user =MyUser.objects.create_user(username__,email__)
                    new_user.groups.add(group)
                    new_user.image = profile.json()['picture']
                    new_user.save()
                    login(request,new_user)
                    return redirect("/")
        return HttpResponse("Google auth callback is  called")
    # except Exception as e:
    #         error_message = str(e) 
    #         return HttpResponse(error_message, status=400)



def buy(request):
    if(request.method == "POST"):
        print(request.POST.get('product_id'), " +++++++++++++++++++")
        print(request.POST.get('Price_ID') , "")
        quantity_ =request.POST.get('quantity')
        stripe.api_key = env("STRIPESECRETKEY")
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': request.POST.get('product_id'),
                    'quantity': quantity_,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/products/buy/success',
            cancel_url="http://localhost:8000/products/buy/canceled",
        )
        print(checkout_session.url , " URL +++++")
        data = {'url': checkout_session.url}
        return JsonResponse(data)
    return JsonResponse("done")




def success_(request):
     return render(request, 'success.html') 




def canceled_(request):
     return render(request, 'canceled.html') 




def reverseastring(request):
    str = "123456789"
    tmp=""
    for char_ in str:
        tmp = char_+ tmp
    return HttpResponse(tmp)



#https://stackoverflow.com/questions/45868120/python-post-request-with-bearer-token
#https://developers.google.com/identity/protocols/oauth2/web-server#httprest_3
#https://stackoverflow.com/questions/20010108/checking-if-username-exists-in-django#:~:text=objects.-,filter(username%3Dusername).,more%20indirection%20and%20unneeded%20verbosity.
#https://github.com/jaredhanson/passport-google-oauth2/blob/master/lib/strategy.js
#https://docs.stripe.com/checkout/quickstart?client=html
#https://docs.stripe.com/testing
#When testing interactively, use a card number, such as 4242 4242 4242 4242. Enter the card number in the Dashboard or in any payment form.
# Use a valid future date, such as 12/34.