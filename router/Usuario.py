from fastapi import APIRouter , Cookie , Response , status
from  pydantic import BaseModel, Field , EmailStr
from cryptography.fernet import Fernet
from typing import Annotated , Union
userRouter = APIRouter(prefix="/user", tags=['user'])

datos=[]
secret_key = Fernet.generate_key()

class Login(BaseModel):
    email: str
    password: str

class usuario(BaseModel):
    nombre:str
    cedula:str
    email:str
    password:str

@userRouter.get("/me", response_model=Union[usuario, dict])
async def user_perfil(userCOOKIE: str = Cookie(default=None)):
    if userCOOKIE:
        clave = userCOOKIE.split("&")
        claves = dict(item.split("=") for item in clave)
        for data in datos:
            if data.password == claves["password"]:
                return data
        return {"mensaje": "perfil no encontrado"}
    return {"mensaje": "cookie no encontrada!."}

@userRouter.post('/login',status_code=status.HTTP_201_CREATED)
async def user_login(usuarioLogin:Login, response:Response):
    """ crear la cookie del login del usuario por contraseña y correo email. """
    cipher = Fernet(secret_key)
    for data in datos:
        if data.email == usuarioLogin.email:
            if data.password == usuarioLogin.password:
                token_str = f"usuario={usuario.email}&password={usuario.password}"
                token = cypher.encrypt(token_str.encode())
                response.set_cookie(key=userCOOKIE,value=token)
                return {"exito":"login exitoso"}
            return response.JSONResponse(content={"info":"usuario no encontrado"},status_code=404)

@userRouter.post('/register', status_code=status.HTTP_201_CREATED)
async def user_register(usuario:usuario,response:Response):
    """
        crear el registro del usuario y creacion del cookie
    """
    cipher = Fernet(secret_key)
    data = f"usuario={usuario.email}&password={usuario.password}"
    token = cypher.encrypt(data.encode())
    
    datos.append(usuario)
    response.set_cookie(key="userCOOKIE",value=token)#usuario.password
    return {"ok":True , "mensaje":"usuario registrado exitosamente!."}