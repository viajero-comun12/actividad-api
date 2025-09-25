from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select

class Usuario(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    contraseña: str
Usuario=[Usuario(id=1,username="admin",contraseña="pacos123")]
app = FastAPI(title="API Login prebas")

@app.post("/login")
def login(username: str, password: str):
    identificador= select(Usuario).where(Usuario.username == username)
    if not username or username.contraseña != contraseña :
        raise HTTPException("Credenciales inválidas")
    return {
        "mensaje": " Acceso permitido",
    }