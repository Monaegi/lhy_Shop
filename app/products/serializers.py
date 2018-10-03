from rest_framework import serializers

from .models import ProductOption, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'pk',
            'img',
        )


class ProductSerializer(serializers.ModelSerializer):
    # image_set = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'pk',
            'category',
            'title',
            'img_cover',
        )


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = (
            'pk',
            'title',
            'price',
            'unit',
        )
