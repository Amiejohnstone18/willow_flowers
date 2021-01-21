import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    town = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total= models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate unique order number 
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update Total
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum']
        self .grand_total = self.order_total 
        self.save()

    def save(self, *args, **kwargs):
        """
        Override Save method
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    Order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    Product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    Lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override Save method
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number