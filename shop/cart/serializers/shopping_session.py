from rest_framework import serializers
from cart.models import ShoppingSession, CartItem
from .cart_item import CartItemSerializer


class ShoppingSessionSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingSession
        fields = ('cart', )
    
    def create(self, validated_data):
        cart = self.context.get('cart')
        shopping_session = ShoppingSession.objects.create(**validated_data)
        for item in cart:
            cart_item = CartItem.objects.create(product_id=item.get('product_id'), 
                                    quantity=item.get('quantity'),
                                    shopping_session=shopping_session)
        return shopping_session

    def get_cart(self, obj):
        print(CartItem.objects.filter(shopping_session=obj).all())
        return CartItemSerializer(instance=CartItem.objects.filter(shopping_session=obj).all(), 
                                  many=True).data
