# Projeto LuizaLabs

## Descrição
Este projeto é uma API REST desenvolvida em Django para gerenciar clientes e seus produtos favoritos.

## Funcionalidades
- **Clientes:** CRUD (Criar, Ler, Atualizar, Excluir) de clientes.
- **Produtos Favoritos:** Adicionar, listar e remover produtos favoritos de um cliente.
- **Produtos:** Listar produtos disponíveis via API externa.

## Requisitos
- Python 3.x
- Django
- Django REST Framework
- `requests`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/LuizaLabs.git

2. Navegue até o diretório do projeto:
   ``bash
   cd clientes-favoritos-api

3. Crie e ative um ambiente virtual
   ``bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

4. Instale as dependências:
   ``bash
   pip install -r requirements.txt

5. Aplique as migraçÕes:
   ``bash
   python manage.py migrate

6. Execute o servidor:
   ``bash
   python manage.py runserver

## Uso

Você pode testar a API usando Postman. Importe a coleção de requisições incluída no projeto:

## Coleção do Postman

Você pode importar as requisições no Postman a partir do arquivo JSON incluído no projeto.

1. Abra o Postman.
2. Vá para a seção de **Coleções** no lado esquerdo.
3. Clique em **Importar** no canto superior esquerdo.
4. Selecione o arquivo `clientes-favoritos-api-postman.json` da pasta `postman` do projeto.
5. Clique em **Importar** para adicionar as requisições à sua coleção no Postman.

O arquivo da coleção está localizado na pasta `postman` do projeto.

## Requisições Disponíveis

GET /clientes/ - Lista de todos os clientes.
POST /clientes/ - Adiciona um novo cliente.
DEL /clientes/{id}/ - Exclui um cliente pelo ID.
POST /auth/token/ - Autentica o usuário e gera um token.
GET /produtos/ - Lista de produtos disponíveis.
POST /clientes/favoritos/ - Adiciona um produto aos favoritos do cliente.
GET /clientes/favoritos/ - Lista produtos favoritos do cliente.
DEL /clientes/favoritos/{produto_id}/ - Remove um produto dos favoritos do cliente.
PUT /clientes/{id}/ - Atualiza as informações de um cliente.

## Testes

Para executar os testes, execute:
   python manage.py test
