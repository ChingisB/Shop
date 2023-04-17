from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'first_name', 
                  'last_name', 'confirm_password', 'is_staff', 'is_superuser']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user
