from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from store.core.exceptions import NotFoundException

from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUsecase
# Importação de ferramentas

# 'List': Para definir tipos de listas
# fastapi: Importa vários componentes do FastAPI.
# pydantic: Importa um tipo UUID (identificador único universal).
# NotFoundException: Uma exceção personalizada.
# ProductIn, ProductOut, ProductUpdate, ProductUpdateOut: 
# Esquemas de dados para produtos.
# ProductUsecase: Lógica de uso para produtos.

router = APIRouter(tags=["products"])
# APIRouter cria um roteador para agrupar os endpoints relacionados aos produtos

# Criar Produto
@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    return await usecase.create(body=body)
# ^ Este endpoint cria um nove produto

# Este endpoint obtém um produto pelo seu ID
@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


# Retorna uma lista de todos os produtos
@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUsecase = Depends()) -> List[ProductOut]:
    return await usecase.query()


# Atualiza um produto existente
@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    return await usecase.update(id=id, body=body)


# Deleta um produto
@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


# Resumo

# POST /: Cria um novo produto.
# GET /{id}: Obtém um produto específico pelo ID.
# GET /: Obtém uma lista de todos os produtos.
# PATCH /{id}: Atualiza um produto específico pelo ID.
# DELETE /{id}: Deleta um produto específico pelo ID.
