
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from products.models import Category, Product, SIZE, Color, Sku


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key', 'created']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['id', 'name', 'is_active']


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sku
        fields = ['id', 'size', 'color', 'is_active']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'status',  'is_active']


