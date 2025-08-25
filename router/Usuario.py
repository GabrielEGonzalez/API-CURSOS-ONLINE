from fastapi import APIRouter , Cookie , Response , status
from  pydantic import BaseModel, Field , EmailStr
from typing import Annotated
userRouter = APIRouter(prefix="/user", tags=['user'])

datos=[
    {"personaID":"password"}
    ]

class Login(BaseModel):
    email: str
    password: str

class usuario(BaseModel):
    pass

@userRouter.get('/me', response_model=usuario)
async def user_perfil(userCOOKIE: str = Cookie(default=None)):
    return {"user":"perfil"}

@userRouter.post('/login',status_code=status.HTTP_201_CREATED)
async def user_login(usuarioLogin:Login, response:Response):
    for data in datos.dict:
        if data['personaID'] == usuarioLogin.password:
            response.set_cookie(key=usuarioLogin.email,value=usuarioLogin.password)
            return {"exito":"login exitoso"}

@userRouter.post('/register')
async def user_register(usuario:Annotated[str,usuario],response:Response):
    pass