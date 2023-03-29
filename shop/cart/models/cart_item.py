from datetime import datetime
from django.db import models
from .shopping_session import ShoppingSession


class CartItem(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())

    class Meta:
        app_label = 'cart'
