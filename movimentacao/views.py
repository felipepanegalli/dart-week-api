from django.db.models import Sum
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movimentacao, Categoria
from .serializers import MovimentacaoSerializer, CategoriaSerializer


class MovimentacaoByAnoMesTotalAPIView(APIView):
    """
    API de Movimentação de Conta Total por Ano e Mês
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, mes=None, ano=None):
        movimentacao = Movimentacao.objects.filter(datamovimentacao__month=mes, datamovimentacao__year=ano)
        receita = movimentacao.filter(categoria_id__tipocategoria='receita').aggregate(Sum('valor'))
        receita = receita['valor__sum'] or 0
        despesa = movimentacao.filter(categoria_id__tipocategoria='despesa').aggregate(Sum('valor'))
        despesa = despesa['valor__sum'] or 0
        total = receita + despesa
        saldo = receita - despesa

        return Response({'receitas': receita, 'despesas': despesa, 'total': total, 'saldo': saldo},
                        status=status.HTTP_200_OK)


class CategoriasAPIView(generics.ListCreateAPIView):
    """
    API de Categorias de movimentação
    """
    permission_classes = [permissions.AllowAny]
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
            return self.queryset.filter(categoria_id__tipocategoria=self.kwargs.get('tipo'))
        if self.kwargs.get('mes') and self.kwargs.get('ano'):
            return self.queryset.filter(datamovimentacao__month=self.kwargs.get('mes'),
                                        datamovimentacao__year=self.kwargs.get('ano'))
        return self.queryset.all()
