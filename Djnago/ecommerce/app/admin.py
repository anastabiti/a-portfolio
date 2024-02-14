#django access database  from The Django admin site   : NEW 
# from django.contrib import admin
from django.contrib import admin

from .models import Products
from .models import Cart
from .models import MyUser

# from django.contrib.auth.models import User




admin.site.register(MyUser)


# admin.site.unregister(User)
# admin.site.register(User)
# admin.site.register(Extended_User)
admin.site.register(Products)
admin.site.register(Cart)