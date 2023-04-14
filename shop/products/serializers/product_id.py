from rest_framework import serializers
from products.models import Product

class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", )