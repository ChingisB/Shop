from django.db import models
import django.utils.timezone as time


class Discount(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    percent = models.DecimalField(decimal_places=2, max_digits=8)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
