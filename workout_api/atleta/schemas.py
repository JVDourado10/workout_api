from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin  # type: ignore

class Atleta(BaseSchema):
  nome: Annotated[str, Field(description='Nome do Atleta', example='João', max_length=50)]
  cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678901', max_length=11)]
  idade: Annotated[int, Field(description='Idade do Atleta', example='24')]
  peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example='65.5')]
  altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example='1.61')]
  sexo: Annotated[str, Field(description='Sexo do Atleta', example='F', max_length=1)]

class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]

