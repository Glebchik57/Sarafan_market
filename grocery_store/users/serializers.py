from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer

User = get_user_model()


class UserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')
