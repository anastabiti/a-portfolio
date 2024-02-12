from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
# django each user can have multiple products
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # CASCADE: When the referenced object is deleted, also delete the objects that have 
    # references to it (when you remove a blog post
    #  for instance, you might want to delete comments as well). SQL equivalent: CASCADE

class Extended_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,
)
    image = models.CharField()