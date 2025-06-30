from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, schemas, crud, auth
from app.database import Base, engine
from app.auth import get_db
from app.routes import personal, aluno  # ⬅️ novo

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(personal.router)  # ⬅️ inclui rotas do personal
app.include_router(aluno.router)     # ⬅️ inclui rotas do aluno

@app.post("/register", response_model=schemas.UsuarioOut)
def registrar(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    if crud.get_usuario_por_email(db, usuario.email):
        raise HTTPException(status_code=400, detail="Email já registrado")
    return crud.criar_usuario(db, usuario)

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = crud.autenticar_usuario(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = auth.criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
