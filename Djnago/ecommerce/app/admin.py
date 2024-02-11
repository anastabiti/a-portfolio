#django access database  from The Django admin site   : NEW 
from django.contrib import admin
from app.models import Products

admin.site.register(Products)