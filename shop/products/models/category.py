from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        app_label = 'products'
