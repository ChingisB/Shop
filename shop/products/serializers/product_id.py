from rest_framework import serializers
from products.models import Product, ProductImage
from .inventory import InventorySerializer
from .discount import DiscountSerializer
from .product_image import ProductImageSerializer
from .rating import RatingSerializer
from .category import CategorySerializer
from .vendor import VendorSerializer
from .product_image import ProductImageSerializer


class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", )