from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.permissions import AdminPermission
from user.serializers import UserSerializer, StaffSerializer


User = get_user_model()


class StaffView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminPermission]


    def get(self, request):
        data = User.objects.filter(is_staff=True).all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_staff=True)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, staff_id):
        staff = get_object_or_404(User, id=staff_id, is_staff=True)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
