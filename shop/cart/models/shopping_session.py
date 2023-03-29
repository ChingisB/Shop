from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ShoppingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())

    class Meta:
        app_label = 'cart'
