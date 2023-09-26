from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'is_staff')

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'is_staff')

    def create(self, validated_data):
        # Encripta la contraseña antes de crear el usuario
        password = validated_data['password']
        hashed_password = make_password(password)

        user = CustomUser.objects.create(
            username=validated_data['username'],
            password=hashed_password,  # Guarda la contraseña encriptada
            is_staff=validated_data.get('is_staff', False)  # Si es necesario
        )

        return user

class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'is_staff')
