from fastapi import FastAPI

from store.core.config import settings
from store.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App() # Cria uma instância da classe App. Isso é necessário para iniciar a aplicação web.
app.include_router(api_router)

# Resumo

# Importações: Importa as dependências necessárias (FastAPI, settings, api_router).
# Classe App: Cria uma nova classe App que herda de FastAPI, adicionando algumas configurações iniciais (versão, título e caminho raiz).
# Instância app: Cria uma instância da classe App.
# Rotas da API: Adiciona o roteador da API à aplicação, permitindo que a aplicação responda a diferentes endpoints definidos no api_router.