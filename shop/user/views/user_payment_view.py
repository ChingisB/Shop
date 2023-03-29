from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from user.models import UserPayment
from user.serializers import UserPaymentSerializer


class UserPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        payment = get_object_or_404(UserPayment, user=request.user)
        serializer = UserPaymentSerializer(instance=payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        if UserPayment.objects.filter(user=user).count() >= 1:
            return Response({"error": "already exists"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = UserPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        payment = get_object_or_404(user=request.user)
        serializer = UserPaymentSerializer(instance=payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        payment = get_object_or_404(UserPayment, user=request.user)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
