from django.db import models
import django.utils.timezone as time


class Inventory(models.Model):
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
