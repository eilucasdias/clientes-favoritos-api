from django.urls import path
from . import views
from .views import ListaProdutos

urlpatterns = [
    path('clientes/', views.ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('clientes/favoritos/', views.ProdutoFavoritoListCreate.as_view(), name='produto-favorito-list-create'),
    path('produtos/', ListaProdutos.as_view(), name='lista-produtos'),
    path('clientes/favoritos/<str:produto_id>/', views.ProdutoFavoritoDelete.as_view(), name='produto-favorito-delete'),
]