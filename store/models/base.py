from datetime import datetime
from decimal import Decimal
from typing import Any
import uuid
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_serializer


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

        return self_dict


# Resumo

# Atributos: A classe CreateBaseModel define atributos comuns para modelos, como id, created_at e updated_at, com valores padrão gerados automaticamente.
# Serialização Personalizada: O método set_model personaliza a serialização do modelo para converter valores Decimal em Decimal128 antes de serializar o objeto. Isso é útil para armazenar corretamente valores decimais de alta precisão no MongoDB.
