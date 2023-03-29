import datetime
from rest_framework import serializers
from products.models import Inventory


class InventorySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.name)
        instance.save()
        return instance
