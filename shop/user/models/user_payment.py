from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    provider = models.CharField(max_length=20)
    account_no = models.CharField(max_length=20)
    expiry = models.DateField()

    class Meta:
        app_label = 'user'
