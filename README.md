instalr las librerias fastapi
sqlmodel
poner los comandos de instalacion en cosnola
luego de eso crea una bdd con el sql model de amague 
crea la bdd con los parametros en este caso

class Usuario(SQLModel):
    id: int | None = Field(default=None, primary_key=True) 
    username: str = Field(index=True, unique=True)
    contraseña: str****
    luego agregas a eso el usuario y contraseña que tu quieras para comprobar 
luego pon la insatalacion del fast api ponemos el app.post para que se carge en docs,
y simplemente compruebas a dentro que lo que ingresaste es los mismo que esta en la bdd quemada o de amgue pones si funcioneo
con un mensaje de son validas o no se pemirio
ef login(username: str, password: str):
    identificador= select(Usuario).where(Usuario.username == username)
    if not username or username.contraseña != contraseña :
        raise HTTPException("Credenciales inválidas")
