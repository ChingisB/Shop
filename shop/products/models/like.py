from django.db import models
from django.contrib.auth import get_user_model
from .product import Product


User = get_user_model()


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'products'
