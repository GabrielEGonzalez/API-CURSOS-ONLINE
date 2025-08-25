from fastapi import APIRouter , Cookie , Response
from  pydantic import BaseModel, Field , EmailStr
userRouter = APIRouter(prefix="/user", tags=['user'])

datos=[
    {"personaID":"password"}
    ]
class Login(BaseModel):
    email: str
    password: str
@userRouter.get('/me')
async def user_perfil():
    return {"user":"perfil"}

@userRouter.post('/login')
async def user_login(usuarioLogin:Login, response:Response):
    for data in datos.dict:
        if data['personaID'] == usuarioLogin.password:
            return data['personaID']

@userRouter.post('/register')
async def user_register():
    pass