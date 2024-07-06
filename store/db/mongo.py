from motor.motor_asyncio import AsyncIOMotorClient

from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient: # retorna instância do cliente MongoDB
        return self.client
# Quando get é chamado, ele retorna o cliente MongoDB que foi criado no construtor.

db_client = MongoClient()


#Resumo

# Importações: Importa AsyncIOMotorClient para trabalhar com MongoDB de forma assíncrona e settings para acessar a URL do banco de dados.
# Classe MongoClient: Define uma classe que encapsula a criação e o acesso a um cliente MongoDB.
# Construtor: Inicializa o cliente MongoDB usando a URL de banco de dados das configurações.
# Método get: Retorna a instância do cliente MongoDB.
# Instância db_client: Cria uma instância da classe MongoClient, que pode ser usada para acessar o cliente MongoDB em outras partes da aplicação.
