from django.shortcuts import get_object_or_404
import django.utils.timezone as time
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from products.models import Vendor
from products.serializers import VendorSerializer
from user.permissions import StaffPermission


class VendorView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated(), StaffPermission()]

    def get(self, request, id=None):
        if id:
            try:
                vendor = Vendor.objects.get(id=id)
            except Vendor.DoesNotExist:
                return Response({"error": "No category with such ID"}, 
                                status=status.HTTP_404_NOT_FOUND)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            vendor = get_object_or_404(Vendor, id=id)
            vendor.name = request.data.get("name", vendor.name)
            vendor.description = request.data.get("description", vendor.description)
            vendor.modified_at = time.now()
            vendor.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        vendor = get_object_or_404(Vendor, id=id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
