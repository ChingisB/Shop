from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from products.models import Rating, Product


class RatingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        try:
            rating = request.data.get('rating')
            Rating.objects.create(product=product, user=request.user, rating=rating)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        rating = get_object_or_404(Rating, user=request.user, product=product)
        try:
            rating.rating = request.data.get('rating')
            rating.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
