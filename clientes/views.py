import requests
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from .models import ProdutoFavorito
from .serializers import ProdutoFavoritoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ListaProdutos(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = requests.get('http://challenge-api.luizalabs.com/api/product/?page=1')
        if response.status_code == 200:
            return Response (response.json())
        else:
            return Response({'error': 'Produto não encontrado.'}, status = response.status_code)

class ProdutoFavoritoListCreate(generics.ListCreateAPIView):
    serializer_class = ProdutoFavoritoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ProdutoFavorito.objects.filter(cliente = self.request.user)
    
    def perform_create(self, serializer):
        produto_id = serializer.validated_data['produto_id']

        if ProdutoFavorito.objects.filter(cliente = self.request.user, produto_id = produto_id).exists():
            raise serializers.ValidationError('Desculpe, o produto já está nos favoritos.')

        response = requests.get(f'http://challenge-api.luizalabs.com/api/product/{produto_id}/')
        if response.status_code == 200:
            serializer.save(cliente = self.request.user)
        else:
            raise serializers.ValidationError('Produto não encontrado.')

class ProdutoFavoritoDelete(generics.DestroyAPIView):
    queryset = ProdutoFavorito.objects.all()
    serializer_class = ProdutoFavoritoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'produto_id'

    def get_queryset(self):
        return ProdutoFavorito.objects.filter(cliente = self.request.user, produto_id = self.kwargs['produto_id'])