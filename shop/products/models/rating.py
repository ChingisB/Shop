from django.db import models
from django.contrib.auth import get_user_model
from .product import Product


User = get_user_model()


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=2)

    class Meta:
        app_label = 'products'
