from django.db import models
from django.conf import settings


# Create your models here.


class Movimentacao(models.Model):
    valor = models.DecimalField('Valor', max_digits=12, decimal_places=2)
    descricao = models.CharField('Descrição', max_length=255)
    datamovimentacao = models.DateTimeField('Data da movimentação')
    categoria_id = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='categorias')
    usuario_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "movimentação"
        verbose_name_plural = "movimentações"
        db_table = "movimentacao"
        ordering = ('datamovimentacao',)


class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=255)
    tipocategoria = models.CharField('Tipo da Categoria', max_length=15)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        db_table = "categoria"
