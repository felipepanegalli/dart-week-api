from django.db.models import Sum
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movimentacao, Categoria
from .serializers import MovimentacaoSerializer, CategoriaSerializer, MovimentacaoPostSerializer


class MovimentacaoByAnoMesTotalAPIView(APIView):
    """
    API de Movimentação de Conta Total por Ano e Mês
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, mes=None, ano=None):
        movimentacao = Movimentacao.objects.filter(datamovimentacao__month=mes, datamovimentacao__year=ano,
                                                   usuario_id=self.request.user.id)
        receita = movimentacao.filter(categoria_id__tipocategoria='receita',
                                      usuario_id=self.request.user.id).aggregate(Sum('valor'))
        receita = receita['valor__sum'] or 0
        despesa = movimentacao.filter(categoria_id__tipocategoria='despesa',
                                      usuario_id=self.request.user.id).aggregate(Sum('valor'))
        despesa = despesa['valor__sum'] or 0
        total = receita + despesa
        saldo = receita - despesa

        return Response(
            {'receitas': float(receita), 'despesas': float(despesa), 'total': float(total), 'saldo': float(saldo)},
            status=status.HTTP_200_OK)


class CategoriasAPIView(generics.ListCreateAPIView):
    """
    API de Categorias de movimentação
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        if self.kwargs.get('tipo'):
            return self.queryset.filter(tipocategoria=self.kwargs.get('tipo'))
        return self.queryset.all()


class MovimentacaoAPIView(generics.ListCreateAPIView):
    """
    API de Movimentação de Conta
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('tipo'):
            return self.queryset.filter(categoria_id__tipocategoria=self.kwargs.get('tipo'),
                                        usuario_id=self.request.user.id)
        if self.kwargs.get('mes') and self.kwargs.get('ano'):
            return self.queryset.filter(datamovimentacao__month=self.kwargs.get('mes'),
                                        datamovimentacao__year=self.kwargs.get('ano'),
                                        usuario_id=self.request.user.id)
        return self.queryset.filter(usuario_id=self.request.user.id).all()

    def post(self, request, *args, **kwargs):
        request.data['usuario_id'] = self.request.user.id
        serializer = MovimentacaoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movimentação criada.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
