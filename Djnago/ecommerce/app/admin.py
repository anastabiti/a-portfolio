#django access database  from The Django admin site   : NEW 
# from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import MyUser

# from django.contrib.auth.models import User




admin.site.register(MyUser)


# admin.site.unregister(User)
# admin.site.register(User)
# admin.site.register(Extended_User)
# admin.site.register(Products)