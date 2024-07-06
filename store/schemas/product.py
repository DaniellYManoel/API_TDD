from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, Field
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    ...


# Resumo

# ProductBase: Define os campos básicos para um produto.
# ProductIn: Usa ProductBase sem adicionar nada novo, normalmente usado para entrada de dados.
# ProductOut: Combina ProductIn e OutSchema para criar um modelo que inclui campos extras e validação para saída de dados.
# convert_decimal_128: Converte valores Decimal para Decimal128.
# Decimal_: Um tipo anotado que usa convert_decimal_128 para conversão pós-validação.
# ProductUpdate: Define campos opcionais para atualização de um produto.
# ProductUpdateOut: Usa ProductOut para saída de dados de atualização.