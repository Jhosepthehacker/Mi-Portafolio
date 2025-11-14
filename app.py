import sqlmodel as sql
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI()
app.title = "Mi Portafolio"

@app.get('/', tags=["Mi Portafolio"])
def home():
    return "Hola, bienvenido(a) a mi portafolio"

@app.post('/accounts', tags=["Registrarse"])
def login(name: str, age: int, gmail: str, password: str):
    data = []
    
    if (len(name) < 1) or (len(age) < 1) or (len(gmail) < 1) or (len(password) < 1):
        return {"Warning": "Por favor complete los formularios"}
    else:
        pass

    data.append(name, age, gmail, password)
