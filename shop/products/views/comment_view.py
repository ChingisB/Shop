from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from products.models import Product, Comment
from products.serializers import CommentSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_view(request, product_id, comment_id=None):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'GET':
        if comment_id:
            serializer = CommentSerializer(instance=get_object_or_404(Comment, id=comment_id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        data = Comment.objects.filter(product=product)
        paginator = PageNumberPagination()
        data = paginator.paginate_queryset(data, request)
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user != request.user:
            return Response({"message": "Cannot delete"}, status=status.HTTP_400_BAD_REQUEST)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
