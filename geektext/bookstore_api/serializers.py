from rest_framework import serializers
from .models import User, CreditCard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'home_address', 'groups', 'user_permissions']


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'name', 'card_number', 'card_type', 'expiration_date']
