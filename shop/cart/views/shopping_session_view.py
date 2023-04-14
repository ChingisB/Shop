import django.utils.timezone as time
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from cart.models import ShoppingSession
from cart.serializers import ShoppingSessionSerializer


class ShoppingSessionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            shopping_session = ShoppingSession.objects.\
                filter(user=request.user).\
                latest("created_at")
            serializer = ShoppingSessionSerializer(instance=shopping_session)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ShoppingSessionSerializer(data=request.data, 
                                               context={'cart': request.data.get('cart')})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            shopping_session = ShoppingSession.objects.\
                filter(user=request.user).\
                latest("created_at")
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShoppingSessionSerializer(data=request.data)
        if serializer.is_valid():
            for key, item in serializer.validated_data.items():
                setattr(shopping_session, key, item)
            shopping_session.modified_at = time.now()
            shopping_session.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
