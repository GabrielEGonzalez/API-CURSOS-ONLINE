from fastapi import APIRouter , Cookie

userRouter = APIRouter(prefix="/user", tags=['user'])

@userRouter.get('/me')
async def user_perfil():
    return {"user":"perfil"}

@userRouter.post('/login')
async def user_login():
    pass

@userRouter.post('/register')
async def user_register():
    pass