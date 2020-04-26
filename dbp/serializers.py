from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from customers.models import Customer
from orders.models import Order, OrderItem
from products.models import Category, Product, SIZE, Color, Sku


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key', 'created']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['is_active', 'id', 'name']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['is_active', 'id', 'name']


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sku
        fields = ['is_active', 'id', 'size', 'color']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['is_active', 'id', 'name', 'category', 'status']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']