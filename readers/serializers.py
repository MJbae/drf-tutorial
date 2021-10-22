from rest_framework import serializers
from .models import Reader, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('detail', 'city')


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('name', 'email', 'addresses')
