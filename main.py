from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que o front-end acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou coloque a URL do seu front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota da API
@app.get("/api")
def read_root():
    return {"mensagem": "API funcionando!"}

# Servindo arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="."), name="static")

# Servindo o front-end principal
@app.get("/")
def serve_front():
    return FileResponse("index.html")
