from rest_framework import serializers

from products.serializers import ProductOptionSerializer, ProductSerializer

__all__ = (
    'CartItemSerializer',
    'CartSerializer',
)


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer(source='product_option.product', read_only=True)
    product_option = ProductOptionSerializer(read_only=True)
    quantity = serializers.IntegerField(min_value=1)


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    amount = serializers.IntegerField()
