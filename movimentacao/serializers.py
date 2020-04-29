from rest_framework import serializers

from core.serializers import UserSerializer
from movimentacao.models import Movimentacao, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome', 'tipocategoria')


class MovimentacaoSerializer(serializers.ModelSerializer):
    categoria_id = CategoriaSerializer(many=False)
    usuario_id = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Movimentacao
        fields = ('id', 'valor', 'descricao', 'datamovimentacao', 'categoria_id', 'usuario_id')


class MovimentacaoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ('id', 'valor', 'descricao', 'datamovimentacao', 'categoria_id', 'usuario_id')
