from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI
from datetime import Datetime


#-----------------------------------------------------------------------

app = FastAPI(title='WorkoutApi')

if _name_ == "main":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)

#-----------------------------------------------------------------------

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atelta", examples="joao", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atelta", examples="12345678911", max_length=11)]
    idade: Annotated[int, Field(description="idade do atelta", examples=25)]
    peso: Annotated[PositiveFloat, Field(description="peso do atelta", examples=75.5)]
    altura: Annotated[PositiveFloat, Field(description="altura do atelta", examples=1.70)]
    altura: Annotated[str, Field(description="sexo do atelta", examples="M", max_length=1)]

#-----------------------------------------------------------------------

class BaseMode(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)

class BaseSchema(BaseModel):
    calss Config:
        extra = "forbid"
        from_attributes = True

class AtletaModel(BaseModel):
    _tablename_ = "ateltas"

    pk_id: Mapped[int] = mapped_column(integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullabel=False)
    CPF: Mapped[str] = mapped_column(String(11), nullabel=False)
    idade: Mapped[int] = mapped_column(Integer, nullabel=False)
    peso: Mapped[float] = mapped_column(Float, nullabel=False)
    altura: Mapped[float] = mapped_column(Float, nullabel=False)
    sexo: Mapped[str] = mapped_column(String(1), nullabel=False)
    created_at: Mapped[datetime]=mapped_column(Datetime, nullabel=False)
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta")
    categoria_id = Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", examples="Scale", max_length=10)]

class CategoriaModel(BaseModel):
    tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullabel=False)
    categoria:Mapped["CategoriaModel"] = relationship(back_populates="atleta")

class CentroTreinamento(BaseModel):
    __table__name = "centros_treinamento"