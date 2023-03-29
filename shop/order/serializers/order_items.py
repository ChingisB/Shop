from rest_framework import serializers
from products.serializers import ProductSerializer
from order.models import OrderItems


class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItems
        fields = ('product', 'quantity')
