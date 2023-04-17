import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import ProductImage, Product
from products.serializers import ProductImageSerializer
from Shop import IMAGE_SERVICE


class ImageView(APIView):
    def get(self, request, image_id=None):
        if not image_id:
            images = ProductImage.objects.all()
            serializer = ProductImageSerializer(images, many=True)
            return Response(serializer.data)
        image = get_object_or_404(ProductImage, id=image_id).image
        return Response(ProductImageSerializer(instance=image).data, 
                        status=status.HTTP_200_OK)
    
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        uploaded_files = request.FILES
        image_files = [file for field, file in uploaded_files.items() 
                       if file.content_type.startswith('image/')]
        data = []
        for image in image_files:
            files = {'image': image}
            response = requests.post(IMAGE_SERVICE + '/upload', files=files)
            product_image = ProductImage.objects.create(product=product, 
                                                        image=image.name)
            data.append(ProductImageSerializer(instance=product_image))
        return Response(ProductImageSerializer(data=data, many=True).data, 
                        status=status.HTTP_201_CREATED)

    def put(self, request, image_id):
        uploaded_files = request.FILES
        image_file = [file for field, file in uploaded_files.items() 
                       if file.content_type.startswith('image/')][0]
        image = get_object_or_404(ProductImage, id=image_id)
        requests.delete(IMAGE_SERVICE + f'delete/{image.image}')
        response = requests.post(IMAGE_SERVICE + 'upload', files={'image': image_file})
        return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, image_id):
        image = get_object_or_404(ProductImage, id=image_id)
        filename = image.image
        response = requests.delete(IMAGE_SERVICE + f'delete/{filename}')
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
