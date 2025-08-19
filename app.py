from fastapi import FastAPI
from router import Usuario

app = FastAPI()
@app.get("/")
async def root():
    return {'hola':'gabriel'}

app.include_router(Usuario.userRouter)