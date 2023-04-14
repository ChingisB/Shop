from django.db.models import Avg
from rest_framework import serializers
from products.models import Product, ProductImage, Inventory, Like, Rating
from .inventory import InventorySerializer
from .discount import DiscountSerializer
from .category import CategorySerializer
from .vendor import VendorSerializer
from .product_image import ProductImageSerializer


class ProductDetailsSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category_id = self.context.get('category_id')
        vendor_id = self.context.get('vendor_id')
        inventory = Inventory.objects.create(quantity=self.context.get('quantity'))
        product = Product.objects.create(category_id=category_id, vendor_id=vendor_id, inventory=inventory, **validated_data)
        return product

    def get_images(self, obj):
        images_queryset = ProductImage.objects.filter(product=obj)
        images_serializer = ProductImageSerializer(instance=images_queryset, many=True)
        return images_serializer.data

    def get_likes(self, obj):
        return Like.objects.filter(product=obj).count()

    def get_rating(self, obj):
        return Rating.objects.filter(product=obj).all().aggregate(Avg('rating'))['rating__avg']
    
    def get_is_liked(self, obj: Product):
        try:
            user = self.context.get('user')
            return obj.like_set.filter(user=user).exists()
        except:
            return False