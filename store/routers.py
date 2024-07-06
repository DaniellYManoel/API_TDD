from fastapi import APIRouter
from store.controllers.product import router as product

api_router = APIRouter()
api_router.include_router(product, prefix="/products")


# Resumo
# Importações: Importa as dependências necessárias (APIRouter e o roteador de produto router).
# Criando api_router: Cria um roteador principal usando APIRouter().
# Incluindo product: Adiciona as rotas do roteador de produto ao roteador principal com o prefixo "/products".