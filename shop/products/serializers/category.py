import datetime
from rest_framework import serializers
from products.models import Category


class CategorySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance: Category, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.modified_at = datetime.datetime.now()
        instance.save()
        return instance
