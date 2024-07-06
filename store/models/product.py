from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...


# Resumo

# ProductModel é uma classe que combina os campos e métodos de ProductIn e CreateBaseModel.
# Isso permite que ProductModel tenha todos os atributos necessários para definir um produto, além de campos adicionais como id, created_at e updated_at.
# Também inclui métodos úteis, como o método de serialização personalizada.
