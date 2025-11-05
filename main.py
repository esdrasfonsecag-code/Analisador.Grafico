from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode trocar por ["https://seusite.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota simples para teste da API
@app.get("/api")
def read_root():
    return {"mensagem": "API funcionando perfeitamente!"}

# Servindo arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Servindo o front-end principal (index.html)
@app.get("/")
def serve_front():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(caminho_arquivo)
