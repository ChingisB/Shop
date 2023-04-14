from django.db import models
import django.utils.timezone as time
from .product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
