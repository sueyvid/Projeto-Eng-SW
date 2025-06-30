from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String, nullable=False)
    tipo = Column(String)  # 'aluno' ou 'personal'

    treinos = relationship("Treino", back_populates="aluno")

class Treino(Base):
    __tablename__ = "treinos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    aluno_id = Column(Integer, ForeignKey("usuarios.id"))

    aluno = relationship("Usuario", back_populates="treinos")
    exercicios = relationship("Exercicio", back_populates="treino")

class Exercicio(Base):
    __tablename__ = "exercicios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    series = Column(Integer)
    repeticoes = Column(Integer)
    treino_id = Column(Integer, ForeignKey("treinos.id"))

    treino = relationship("Treino", back_populates="exercicios")
