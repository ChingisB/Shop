from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from user.serializers import UserSerializer


User = get_user_model()


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'})

        token, _ = Token.objects.get_or_create(user=user)

        serializer = UserSerializer(user)

        return Response({'token': token.key, 'user': serializer.data})
