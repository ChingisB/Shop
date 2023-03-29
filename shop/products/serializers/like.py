from rest_framework import serializers
from user.serializers import UserSerializer
from products.models import Like
from .product import ProductSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Like
        fields = "__all__"