import json
import requests
from django.shortcuts import get_object_or_404
from django.db.models import Q
import django.utils.timezone as time
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from products.models import Product, ProductImage, Category, Vendor
from products.serializers import ProductSerializer, ProductDetailsSerializer
from user.permissions import StaffPermission
from Shop import IMAGE_SERVICE

class ProductView(APIView):
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method != "GET":
            return [IsAuthenticated(), StaffPermission()]
        return []

    def post(self, request):
        uploaded_files = request.FILES
        image_files = [file for field, file in uploaded_files.items()
                       if file.content_type.startswith('image/')]
        data = json.loads(request.data.get('product_info'))
        serializer = ProductDetailsSerializer(data=data, context={
            'category_id': data['category_id'],
            'vendor_id': data['vendor_id'],
            'quantity': data['quantity'],
        })
        if serializer.is_valid():
            product = serializer.save()
            for image in image_files:
                image_name = image.name.split('.')
                image_name[0] += str(product.id)
                image.name = '.'.join(image_name)
                files = {'image': image}
                response = requests.post(IMAGE_SERVICE + 'upload', files=files)
                ProductImage.objects.create(image=image.name, 
                                            product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, product_id=None):
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "No product with such ID"}, status=404)
            serializer = ProductDetailsSerializer(product, context={'user': request.user})
            return Response(serializer.data)
        products = Product.objects.all()


        category = request.query_params.get('category')
        if category:
            products = products.filter(category__name=category)


        vendor = request.query_params.get('vendor')
        if vendor:
            products = products.filter(vendor__name=vendor)


        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        elif min_price:
            products = products.filter(price__gte=min_price)
        elif max_price:
            products = products.filter(price__lte=max_price)


        name = request.query_params.get('name')
        if name:
            products = products.filter(Q(name__icontains=name) | Q(description__icontains=name))

        sorting = request.query_params.get('sorting')
        order = request.query_params.get('order', 'DESC')
        if sorting == 'price':
            if order == 'DESC':
                products = products.order_by('-price')
            else:
                products = products.order_by('price')

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated_products, context={'user': request.user}, many=True)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        try:
            # Well I don't want to bother about special serializer method
            name = request.data.get('name', product.name)
            description = request.data.get('description', product.description)
            price = request.data.get('price', product.price)
            category_id = request.data.get('category_id', product.category_id)
            vendor_id = request.data.get('vendor_id', product.vendor_id)
            quantity = request.data.get('quantity', product.inventory.quantity)
            category = get_object_or_404(Category, id=category_id)
            vendor = get_object_or_404(Vendor, id=vendor_id)
            product.name = name
            product.description = description
            product.price = price
            product.category = category
            product.vendor = vendor
            product.inventory.quantity = quantity
            product.modified_at = time.now()
            product.inventory.save()
            product.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
