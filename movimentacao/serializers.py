from rest_framework import serializers

from core.serializers import UserSerializer
from movimentacao.models import Movimentacao, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome', 'tipocategoria')


class MovimentacaoSerializer(serializers.ModelSerializer):
    # categorias = CategoriaSerializer(many=False, read_only=True)
    # usuarios = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Movimentacao
        fields = ('id', 'valor', 'descricao', 'datamovimentacao', 'categoria_id', 'usuario_id')

    def create(self, validated_data):
        movimentacao = Movimentacao(
            valor=validated_data['valor'],
            descricao=validated_data['descricao'],
            datamovimentacao=validated_data['datamovimentacao'],
            categoria_id=validated_data['categoria_id'],
            usuario_id=validated_data['usuario_id'],
        )
        movimentacao.save()
        return movimentacao
