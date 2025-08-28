from fastapi import APIRouter , Cookie , Response , status
from  pydantic import BaseModel, Field , EmailStr
from typing import Annotated , Union
userRouter = APIRouter(prefix="/user", tags=['user'])

datos=[]

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
        for data in datos:
            if data.password == userCOOKIE:
                return data
        return {"mensaje": "perfil no encontrado"}
    return {"mensaje": "cookie no encontrada!."}

@userRouter.post('/login',status_code=status.HTTP_201_CREATED)
async def user_login(usuarioLogin:Login, response:Response):
    """ crear la cookie del login del usuario por contraseña y correo email. """
    for data in datos:
        if data.email == usuarioLogin.email:
            if data.password == usuarioLogin.password:
                response.set_cookie(key=usuarioLogin.email,value=usuarioLogin.password)
                return {"exito":"login exitoso"}
            return response.JSONResponse(content={"info":"usuario no encontrado"},status_code=404)

@userRouter.post('/register', status_code=status.HTTP_201_CREATED)
async def user_register(usuario:usuario,response:Response):
    """
        crear el registro del usuario y creacion del cookie
    """
    datos.append(usuario)
    response.set_cookie(key="userCOOKIE",value=usuario.password)
    return {"ok":True , "mensaje":"usuario registrado exitosamente!."}