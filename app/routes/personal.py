from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, auth
from app.auth import get_db, get_usuario_atual

router = APIRouter(prefix="/personal", tags=["Personal"])

# Middleware: só permite personal
def verificar_personal(usuario: models.Usuario = Depends(get_usuario_atual)):
    if usuario.tipo != "personal":
        raise HTTPException(status_code=403, detail="Acesso restrito a personal trainers")
    return usuario

@router.post("/criar_treino", response_model=schemas.Treino)
def criar_treino(
    treino: schemas.TreinoCreate,
    aluno_id: int,
    db: Session = Depends(get_db),
    personal: models.Usuario = Depends(verificar_personal)
):
    aluno = db.query(models.Usuario).filter(models.Usuario.id == aluno_id, models.Usuario.tipo == "aluno").first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    novo_treino = models.Treino(nome=treino.nome, aluno_id=aluno.id)
    db.add(novo_treino)
    db.commit()
    db.refresh(novo_treino)

    for ex in treino.exercicios:
        novo_ex = models.Exercicio(
            nome=ex.nome,
            series=ex.series,
            repeticoes=ex.repeticoes,
            treino_id=novo_treino.id
        )
        db.add(novo_ex)

    db.commit()
    db.refresh(novo_treino)
    return novo_treino
