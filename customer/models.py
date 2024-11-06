from django.db import models

from seller.models import Product


# Create your models here.


class Cart(models.Model):
    date_added = models.DateField(auto_now_add=True)
    session_id = models.CharField(max_length=255)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
