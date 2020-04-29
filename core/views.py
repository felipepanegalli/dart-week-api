from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserAPIView(APIView):
    """
    API de Manutenção de usuários
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Usuário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)
