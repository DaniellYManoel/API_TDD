from pydantic_settings import BaseSettings, SettingsConfigDict
# pydantic_settings e BaseSettings são usado para definir classes de configuração, e SettingsConfigDict é utilizado para configurar como essas configurações são carregadas.


# Esta classe define as configurações da aplicação
class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()


#Resumo
# A classe Settings define as configurações da aplicação usando BaseSettings do Pydantic.
# PROJECT_NAME e ROOT_PATH têm valores padrão.
# DATABASE_URL é um campo obrigatório e deve ser fornecido.
# SettingsConfigDict é usado para especificar que as variáveis de ambiente devem ser carregadas de um arquivo .env.
# Uma instância settings da classe Settings é criada, carregando e validando as configurações automaticamente.
