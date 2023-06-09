from django.db import models
import django.utils.timezone as time
from django.contrib.auth import get_user_model
from .product import Product


User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)

    class Meta:
        app_label = 'products'
