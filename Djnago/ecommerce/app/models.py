from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# # from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    Price_ID=models.CharField(max_length=1000, default="0")
# django each user can have multiple products
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # CASCADE: When the referenced object is deleted, also delete the objects that have 
    # references to it (when you remove a blog post
    #  for instance, you might want to delete comments as well). SQL equivalent: CASCADE


#blank=True so is not required 

# Create your models here. https://servidorandycode.medium.com/django-overwrite-user-model-b91bcbbbefa2
class MyUser(AbstractUser):
    print("Myuser is called !+_+_+_+_+_+_+_+_+_+_++_+_+_+_+_+_+__+_+_+_")
    # Some rules adding username
    username_validator = UnicodeUsernameValidator()
    valid_email = EmailValidator()
    #Custom Field
    image =models.URLField( unique=False, null=True,blank=True) #image URL uploaded 
    email = models.EmailField(('email'), max_length=80, unique=True,validators=[valid_email],    blank=False)\
    
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
        blank=True # Same code that has django as a default only added this to say can be an empty value
    )
    # group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    # Field for login
    USERNAME_FIELD = 'email'  # use email to login
    # Field for command createsuperuser
    REQUIRED_FIELDS = ['username','first_name','last_name']
    def __str__(self):
        return f"{self.email}"
    


class Cart(models.Model):
    buyer= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    quantity= models.IntegerField(default=0)
    date =  models.DateField(datetime.now().date())