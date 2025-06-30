from sqlalchemy.orm import Session
from app import models, schemas, auth

def get_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    senha_hash = auth.gerar_hash_senha(usuario.senha)
    db_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=senha_hash,
        tipo=usuario.tipo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = get_usuario_por_email(db, email)
    if not usuario or not auth.verificar_senha(senha, usuario.senha_hash):
        return None
    return usuario
