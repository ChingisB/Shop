from django.db.models import Avg
from rest_framework import serializers
from products.models import Product, ProductImage, Rating
from .inventory import InventorySerializer
from .discount import DiscountSerializer
from .product_image import ProductImageSerializer
from .category import CategorySerializer
from .vendor import VendorSerializer
from .product_image import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    discount = DiscountSerializer()
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    vendor = VendorSerializer()
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
    
    def get_image(self, obj):
        image = ProductImage.objects.filter(product=obj).first()
        image_serializer = ProductImageSerializer(instance=image)
        return image_serializer.data

    def get_rating(self, obj):
        return Rating.objects.filter(product=obj).all().aggregate(Avg('rating'))['rating__avg']
