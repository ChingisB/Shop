from rest_framework import serializers
from products.models import Discount


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'name', 'description', 'percent', 'active')
