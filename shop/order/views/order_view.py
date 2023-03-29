from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from order.models import OrderDetails
from order.serializers import OrderDetailsSerialzer, PaymentDetailsSerializer


class OrderView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, order_id=None):
        if order_id:
            order = get_object_or_404(OrderDetails, id=order_id)
            serializer = OrderDetailsSerialzer(instance=order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        orders = OrderDetails.objects.filter(user=request.user)
        serializer = OrderDetailsSerialzer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        user = request.user
        serializer = OrderDetailsSerialzer(data=request.data, 
                                           context={'items': request.data.get('items')})
        payment = PaymentDetailsSerializer(data=request.data.get('payment'))
        if payment.is_valid() and serializer.is_valid():
            payment = payment.save()
            serializer.save(user=user, payment=payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
