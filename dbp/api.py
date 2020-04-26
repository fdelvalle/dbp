from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dbp.serializers import TokenSerializer


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
        serializer = TokenSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})