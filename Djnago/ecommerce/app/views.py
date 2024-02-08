from django.http import HttpResponse
    
def home(request):
    return HttpResponse ("WELCOME TO E-COMMERCE")
def post_auth(request):
    return HttpResponse(request.method)
