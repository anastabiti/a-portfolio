# from django.db import models
# # from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# class Products(models.Model):
#     name=models.CharField(max_length=50)
#     price=models.IntegerField()
# # django each user can have multiple products
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     # CASCADE: When the referenced object is deleted, also delete the objects that have 
#     # references to it (when you remove a blog post
#     #  for instance, you might want to delete comments as well). SQL equivalent: CASCADE

# class Extended_User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,
# )
#     image = models.CharField()


# class User(AbstractUser):
#     image = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google.png/640px-Google.png')
#     # pass
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here. https://servidorandycode.medium.com/django-overwrite-user-model-b91bcbbbefa2
class MyUser(AbstractUser):
    # Some rules adding username
    username_validator = UnicodeUsernameValidator()

    #Custom Field
    email = models.EmailField(_('email'), max_length=80, unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True # Same code that has django as a default only added this to say can be an empty value
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    # Field for login
    USERNAME_FIELD = 'email'
    image =models.URLField( unique=False, null=True) #image URL uploaded 
    # Field for command createsuperuser
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return f"{self.email}"