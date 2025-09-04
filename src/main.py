from fastapi import FastAPI
from scraper import coletar_noticias

app = FastAPI()  

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}

@app.get("/noticias")
def listar_noticias():
    return {"noticias": coletar_noticias()}
