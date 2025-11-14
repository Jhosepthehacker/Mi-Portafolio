import sqlmodel as sql
import json
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
    message = {
        "Warning": "Por favor complete los formularios"
    }
    
    if (len(name) < 1) or (len(age) < 1) or (len(gmail) < 1) or (len(password) < 1):
        with open('package.json', 'w') as file_json:
            json.dump(message, file_json, indent=4)
    else:
        pass

    data.append(name, age, gmail, password)
    
