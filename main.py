from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rota_principal():
    return{"message": "Hello World!"}

@app.get('/teste')
def rota_teste():
    return{"message":"Tá funcionando"}