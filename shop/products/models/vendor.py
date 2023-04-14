from django.db import models
import django.utils.timezone as time


class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
