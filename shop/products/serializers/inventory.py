import django.utils.timezone as time
from rest_framework import serializers
from products.models import Inventory


class InventorySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)

    def update(self, instance: Inventory, validated_data):
        instance.quantity = validated_data.get('quantity', instance.name)
        instance.modified_at = time.now()
        instance.save()
        return instance
