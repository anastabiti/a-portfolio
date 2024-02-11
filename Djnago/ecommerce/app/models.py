from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


# django each user can have multiple products
#     from django.db import models
# from django.contrib.auth.models import User

# class Product(models.Model):
#     seller = models.ForeignKey(User, on_delete=models.CASCADE)
#     # Add other product-related fields