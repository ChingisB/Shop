from rest_framework import serializers
from user.models import UserPayment
from .user import UserSerializer


class UserPaymentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserPayment
        fields = "__all__"
