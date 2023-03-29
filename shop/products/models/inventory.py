from datetime import datetime
from django.db import models


class Inventory(models.Model):
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
