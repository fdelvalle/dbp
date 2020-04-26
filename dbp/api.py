from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from customers.models import Customer
from dbp import serializers
from orders.models import Order, OrderItem
from products.models import Product, Category, Color, Sku


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = serializers.ColorSerializer
    permission_classes = [IsAuthenticated]


class SkuViewSet(ModelViewSet):
    queryset = Sku.objects.all()
    serializer_class = serializers.SkuSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [IsAuthenticated]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


class TokenViewSet(ViewSet):
    """
    API de Token de acesso

    Payload POST:

    {
    "username": xxxxxxxx,
    "password": ********
    }

    Para usar informar a Key no Header:

    Authorization:Token 979779799yhouhkhy7ihkd334d55f66b677n7777h

    """
    queryset = Token.objects.none()
    serializer_class = AuthTokenSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = Token.objects.filter(user=self.request.user)
        return queryset

    def list(self, request):
        queryset = self.get_object()
        serializer = serializers.TokenSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})