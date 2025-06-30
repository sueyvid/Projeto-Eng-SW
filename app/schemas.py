from pydantic import BaseModel
from typing import List

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str
    tipo: str  # aluno ou personal

class UsuarioOut(UsuarioBase):
    id: int
    tipo: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ExercicioBase(BaseModel):
    nome: str
    series: int
    repeticoes: int

class Exercicio(ExercicioBase):
    id: int
    class Config:
        from_attributes = True

class TreinoBase(BaseModel):
    nome: str

class TreinoCreate(TreinoBase):
    exercicios: List[ExercicioBase] = []

class Treino(TreinoBase):
    id: int
    exercicios: List[Exercicio] = []
    class Config:
        from_attributes = True
