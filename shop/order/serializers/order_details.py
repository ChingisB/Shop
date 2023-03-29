from rest_framework import serializers
from order.models import OrderDetails, OrderItems
from user.serializers import UserSerializer
from products.models import Product
from .payment_details import PaymentDetailsSerializer
from .order_items import OrderItemsSerializer


class OrderDetailsSerialzer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payment = PaymentDetailsSerializer()
    items = serializers.SerializerMethodField()
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderDetails
        fields = "__all__"
        read_only = ('total', )

    def create(self, validated_data):
        items = self.context.get('items')
        order = OrderDetails.objects.create(**validated_data)
        total = 0
        for item in items:
            product_id = item.get('product_id')
            quantity=item.get('quantity')
            OrderItems.objects.create(product_id=product_id, 
                                      quantity=quantity, order=order)
            total += Product.objects.filter(id=product_id).first().price * quantity
        order.total = total
        order.save()
        return order


    def get_items(self, obj):
        items = OrderItemsSerializer(instance=
                                     OrderItems.objects.filter(order=obj), 
                                     many=True)
        return items.data
