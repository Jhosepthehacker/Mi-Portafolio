from fastapi import FastAPI

app = FastAPI()
app.title = "Mi Portafolio"

@app.get('/', tags=["Home"])
def home():
    return "Hola, bienvenido(a) a mi portafolio"
