from django.http import HttpResponse
    
def home(request):
    return HttpResponse ("WELCOME TO E-COMMERCE")
def post_auth(request):
    print("post auth is called")
    return HttpResponse(request.method)
