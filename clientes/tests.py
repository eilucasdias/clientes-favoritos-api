from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cliente, ProdutoFavorito
from django.contrib.auth.models import User

class ClienteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_cliente(self):
        url = reverse('cliente-list-create')
        data = {'nome': 'Novo Cliente', 'email': 'novo@cliente.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nome, 'Novo Cliente')

    def test_list_clientes(self):
        Cliente.objects.create(nome='Cliente Existente', email='existente@cliente.com')
        url = reverse('cliente-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class ProdutoFavoritoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.produto_url = 'http://challenge-api.luizalabs.com/api/product/69e2f68f-20cc-b9c0-8365-89928a2dcf88/'

    def test_add_produto_favorito(self):
        url = reverse('produto-favorito-list-create')
        data = {
            'produto_id': '69e2f68f-20cc-b9c0-8365-89928a2dcf88',
            'title': 'Produto Teste',
            'brand': 'Marca Teste',
            'price': '99.99',
            'image': 'http://example.com/produto.jpg',
            'reviewScore': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProdutoFavorito.objects.count(), 1)

    def test_list_produtos_favoritos(self):
        ProdutoFavorito.objects.create(
            cliente=self.user,
            produto_id='69e2f68f-20cc-b9c0-8365-89928a2dcf88',
            title='Produto Teste',
            brand='Marca Teste',
            price='99.99',
            image='http://example.com/produto.jpg'
        )
        url = reverse('produto-favorito-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_produto_favorito(self):
        ProdutoFavorito.objects.create(
            cliente=self.user,
            produto_id='69e2f68f-20cc-b9c0-8365-89928a2dcf88',
            title='Produto Teste',
            brand='Marca Teste',
            price='99.99',
            image='http://example.com/produto.jpg'
        )
        url = reverse('produto-favorito-delete', kwargs={'produto_id': '69e2f68f-20cc-b9c0-8365-89928a2dcf88'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ProdutoFavorito.objects.count(), 0)
