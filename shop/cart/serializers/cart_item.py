from rest_framework import serializers
from cart.models import CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = '__all__'
