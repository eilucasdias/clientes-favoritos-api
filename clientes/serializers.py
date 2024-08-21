from rest_framework import serializers
from .models import Cliente
from .models import ProdutoFavorito

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email']

class ProdutoFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoFavorito
        fields = ['id', 'cliente', 'produto_id', 'title', 'brand', 'price', 'image', 'reviewScore']
        read_only_fields = ['cliente']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['reviewScore'] is None:
            representation['reviewScore'] = 'Não disponível'
        return representation