from django.urls import path

from .views import MovimentacaoAPIView, CategoriasAPIView, MovimentacaoByAnoMesTotalAPIView

urlpatterns = [
    path('categorias/', CategoriasAPIView.as_view(), name='categorias'),
    path('categorias/<str:tipo>/', CategoriasAPIView.as_view(), name='categorias-by-tipo'),

    path('movimentacoes/', MovimentacaoAPIView.as_view(), name='movimentacoes'),
    path('movimentacoes/<str:tipo>/', MovimentacaoAPIView.as_view(), name='movimentacoes-by-tipo'),
    path('movimentacoes/<int:mes>/<int:ano>/', MovimentacaoAPIView.as_view(), name='movimentacoes-by-month'),
    path('movimentacoes/total/<int:mes>/<int:ano>/', MovimentacaoByAnoMesTotalAPIView.as_view(),
         name='movimentacoes-total-month'),

]
