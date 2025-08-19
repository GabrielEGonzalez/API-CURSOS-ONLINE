from fastapi import FastAPI
from  pydantic import BaseModel, Field , EmailStr


class userBase(BaseModel):
    nombre: str = Field(...,title="nombre del usuario",examples=["john"])
    apellido: str = Field(...,title="apellido del usuario",examples=["Doe"])
    cedula: str
    email : EmailStr = Field(...)


class userOUT(userBase):
    id: int

class userBD(userBase):
    password: str = Field(...)