from rest_framework import serializers
from products.models import Vendor


class VendorIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id')
