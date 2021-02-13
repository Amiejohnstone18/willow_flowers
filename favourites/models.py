from django.db import models
from products.models import Product
from profiles.models import UserProfile


# Create your models here.
class Favourite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
