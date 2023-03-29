from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=70)
    address = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)

    class Meta:
        app_label = 'user'
