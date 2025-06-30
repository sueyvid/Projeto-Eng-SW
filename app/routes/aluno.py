from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.auth import get_db, get_usuario_atual

router = APIRouter(prefix="/aluno", tags=["Aluno"])

@router.get("/meus_treinos", response_model=list[schemas.Treino])
def listar_treinos(
    usuario: models.Usuario = Depends(get_usuario_atual),
    db: Session = Depends(get_db)
):
    if usuario.tipo != "aluno":
        raise HTTPException(status_code=403, detail="Acesso restrito a alunos")

    treinos = db.query(models.Treino).filter(models.Treino.aluno_id == usuario.id).all()
    return treinos

@router.get("/treino/{treino_id}/exercicios", response_model=list[schemas.Exercicio])
def listar_exercicios(
    treino_id: int,
    usuario: models.Usuario = Depends(get_usuario_atual),
    db: Session = Depends(get_db)
):
    treino = db.query(models.Treino).filter(models.Treino.id == treino_id, models.Treino.aluno_id == usuario.id).first()
    if not treino:
        raise HTTPException(status_code=404, detail="Treino não encontrado")
    return treino.exercicios
