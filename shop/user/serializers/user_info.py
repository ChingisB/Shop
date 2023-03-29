from rest_framework import serializers
from user.models import UserInfo
from .user import UserSerializer


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('country', 'city', 'address', 'postal_code', 'telephone')

