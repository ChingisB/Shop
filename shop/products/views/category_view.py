from django.shortcuts import get_object_or_404
import django.utils.timezone as time
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from products.models import Category
from products.serializers import CategorySerializer
from user.permissions import StaffPermission


class CategoryView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated(), StaffPermission()]

    def get(self, request, id=None):
        if id:
            try:
                category = Category.objects.get(id=id)
            except Category.DoesNotExist:
                return Response({"error": "No category with such ID"}, status=404)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category.name = serializer['name'].value
            category.description = serializer['description'].value
            category.modified_at = time.now()
            category.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
