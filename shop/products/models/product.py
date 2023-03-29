from datetime import datetime
from django.db import models
from .inventory import Inventory
from .discount import Discount
from .category import Category
from .vendor import Vendor


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
