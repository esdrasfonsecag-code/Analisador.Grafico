from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Criando a aplicação FastAPI
app = FastAPI(title="Analisador Gráfico")

# Configuração de CORS (opcional, útil para front-end)
origins = [
    "*",  # Permite qualquer origem, se for para produção, restringir
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Modelos de dados
# -----------------------
class AnaliseRequest(BaseModel):
    time_a: str
    time_b: str
    estatisticas: dict

# -----------------------
# Rotas
# -----------------------

# Rota raiz
@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}

# Exemplo de rota de análise
@app.post("/analisar")
def analisar(request: AnaliseRequest):
    # Aqui você pode colocar sua lógica de análise
    # Por enquanto, apenas retorna os dados recebidos
    resultado = {
        "time_a": request.time_a,
        "time_b": request.time_b,
        "chance_over_2_5": 92  # Exemplo fixo
    }
    return resultado

# Rota de teste simples
@app.get("/status")
def status():
    return {"status": "online"}
