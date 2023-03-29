from rest_framework import serializers
from django.core.files.storage import FileSystemStorage
from products.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"