from typing import List
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exceptions import NotFoundException


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get() # Obtém o cliente MongoDB
        self.database: AsyncIOMotorDatabase = self.client.get_database() # Acessa o banco de dados
        self.collection = self.database.get_collection("products") # Acessa a coleção de produtos no banco de dados


    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())
    # create: Cria um novo produto.
    # ProductModel: Converte os dados do ProductIn para um modelo de produto.
    # insert_one: Insere o modelo de produto no banco de dados.
    # ProductOut: Retorna o produto recém-criado no formato de saída.


    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)
    # get: Recupera um produto pelo ID.
    # find_one: Busca o produto pelo ID na coleção.
    # Erro: Se não encontrar, lança uma exceção NotFoundException.
    # ProductOut: Retorna o produto encontrado no formato de saída


    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]
    # query: Recupera todos os produtos.
    # find: Busca todos os produtos na coleção.
    # Compreensão de Lista: Converte cada item encontrado em um ProductOut e retorna uma lista desses produtos.

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)
    # update: Atualiza um produto pelo ID.
    # find_one_and_update: Encontra e atualiza o produto pelo ID.
    # "$set": Define os campos a serem atualizados, excluindo campos None.
    # ProductUpdateOut: Retorna o produto atualizado no formato de saída.

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False
# delete: Exclui um produto pelo ID.
# find_one: Verifica se o produto existe.
# Erro: Se não encontrar, lança uma exceção NotFoundException.
# delete_one: Exclui o produto.
# Retorno: Retorna True se o produto foi excluído, False caso contrário.

product_usecase = ProductUsecase()

# Instância: Cria uma instância de ProductUsecase que pode ser usada em outras partes do seu código para gerenciar produtos.
