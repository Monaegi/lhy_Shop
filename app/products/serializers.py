from rest_framework import serializers

from .models import ProductOption, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'category',
            'title',
        )


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = (
            'pk',
            'title',
            'price',
            'unit',
            'price_per_unit',
        )
