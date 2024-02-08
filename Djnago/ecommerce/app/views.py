from django.http import HttpResponse
# create a user
from django.contrib.auth.models import User

def home(request):
    return HttpResponse ("WELCOME TO E-COMMERCE")
def post_auth(request):
    print("post auth is called")
    return HttpResponse(request.method)
def create_user(request):
    if(request.method == 'POST'):
        user =User.objects.create_user(request.POST.get("username") ,request.POST.get("email"),request.POST.get("password"))
        user.save()
    return HttpResponse(request.POST)
    
