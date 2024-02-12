#django access database  from The Django admin site   : NEW 
# from django.contrib import admin
from app.models import Products
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app.models import Extended_User






# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class extended_userinline(admin.StackedInline):
#     model = Extended_User
#     can_delete = False
#     verbose_name_plural = "extended_user"


# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [extended_userinline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Extended_User)
admin.site.register(Products)