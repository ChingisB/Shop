from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import Product, Like
from products.serializers import ProductSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def liked_products(request):
    user = request.user
    likes = Like.objects.filter(user=user)
    products = Product.objects.filter(like__in=likes)
    serializer = ProductSerializer(instance=products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)