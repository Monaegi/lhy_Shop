from rest_framework import serializers

from products.serializers import ProductOptionSerializer, ProductSerializer

__all__ = (
    'CartProductOptionSerializer',
    'CartProductSerializer',
    'CartSerializer',
)


class CartProductOptionSerializer(serializers.Serializer):
    option = ProductOptionSerializer(read_only=True)
    quantity = serializers.IntegerField(min_value=1)


class CartProductSerializer(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    options = CartProductOptionSerializer(many=True, read_only=True)


class CartSerializer(serializers.Serializer):
    items = CartProductSerializer(many=True, read_only=True)
    amount = serializers.IntegerField()
