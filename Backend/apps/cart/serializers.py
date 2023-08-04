from rest_framework.fields import ImageField
from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    image=ImageField(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'