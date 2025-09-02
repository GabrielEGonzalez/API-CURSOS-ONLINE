from fastapi import APIRouter,Response,Cookie
from pydantic import BaseModel,Field
from datetime import time

cursoRouter = APIRouter(prefix="/curso", tags=['curso'])

curso = []

class Curso(BaseModel):
    id:int
    nombre_Curso:str
    horario:time
    categoria:str
"""
#Cursos:

`POST /cursos`: Crear un curso (Instructor)
`GET /cursos`: Lista de cursos (query: categoría, orden)
`GET /cursos/{curso_id}`: Detalles de un curso (path)
`PUT /cursos/{id}`: Editar curso (body)
"""

@cursoRouter.post("/",status_code=201)
async def crear_curso(userCookie:Cookie(),curso:Curso):
    perfildata = dict( item.split("=") for item in userCookie.split("&"))
    if perfildata["rol"] == "Instructor":
      curso.append(curso)
      Response.status_code=201
      return {"mensaje":"curso creado exitosamente!" ,"ok":True}
    Response.status_code=401
    return {"mensaje":"curso no creado","ok":False,"rol": f"no {perfildata['rol']} autorizado"}