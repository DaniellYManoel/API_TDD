from datetime import datetime
from decimal import Decimal
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True # Crie um modelo a partir de atributos de uma instância de classeou de um dicionário.
# Herança de 'BaseModel': 'BaseSchemaMixin' herda de 'BaseModel', o que significa que é uma classe Pydantic
# Classe Interna 'config': A classe interna 'config' contém contém configurações para o Pydantic


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator(mode="before")
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data # Retorna o dicionário modificado.


# Atributos da Classe
# id: Um identificador único universal (UUID4).
# created_at: A data e hora em que o objeto foi criado.
# updated_at: A data e hora em que o objeto foi atualizado.
# Field() é usado para declarar campos no Pydantic.

# Método set_schema
# Decorador @model_validator(mode="before"): Este decorador indica que set_schema é um validador que deve ser executado antes de qualquer outra validação.

# Lógica do Método
# def set_schema(cls, data):: Define um método de classe chamado set_schema que aceita data, um dicionário.
# Loop: Itera sobre os itens do dicionário data.
# if isinstance(value, Decimal128):: Verifica se o valor é uma instância de Decimal128.
# data[key] = Decimal(str(value)): Converte o valor Decimal128 para Decimal.
