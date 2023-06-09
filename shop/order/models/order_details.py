from django.db import models
import django.utils.timezone as time
from django.contrib.auth import get_user_model
from .payment_details import PaymentDetails


User = get_user_model()


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=time.now)
    modified_at = models.DateTimeField(default=time.now)

    class Meta:
        app_label = 'order'
