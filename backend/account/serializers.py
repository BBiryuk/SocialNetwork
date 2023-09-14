from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('avatar', 'following', 'friends', 'bio')


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'account')
        extra_kwargs = {'password': {'write_only': True}}
