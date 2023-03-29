from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import Product, Like


@api_view(['POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def like_view(request, product_id, like_id=None):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        like = Like.objects.filter(product=product, user=user)
        if like:
            return Response({"message": "user already liked"}, status=status.HTTP_202_ACCEPTED)
        Like.objects.create(user=user, product=product)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        like = get_object_or_404(Like, product=product, user=user)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
