from rest_framework import serializers
from order.models import PaymentDetails


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"
