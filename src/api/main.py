from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI(title="Datathon - API de Recomendação de Oferta")

# Carrega o estado do bandit uma única vez, na inicialização do servidor
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "bandit_state.json")

with open(MODEL_PATH, "r", encoding="utf-8") as f:
    bandit_state = json.load(f)

BRACOS = ["Deposito_Turbo", "Deposito_Turbo_Plus", "Consultoria_Invest"]


def obter_segmento(idade: int) -> str:
    if idade <= 35:
        return "jovem"
    elif idade < 55:
        return "meia_idade"
    else:
        return "idoso"


class ClienteRequest(BaseModel):
    idade: int


class RecomendacaoResponse(BaseModel):
    segmento: str
    oferta_recomendada: str
    taxa_conversao_estimada: float


@app.post("/recomendar", response_model=RecomendacaoResponse)
def recomendar_oferta(cliente: ClienteRequest):
    segmento = obter_segmento(cliente.idade)
    estado_segmento = bandit_state[segmento]

    taxas_estimadas = {
        braco: estado_segmento["alpha"][braco] / (estado_segmento["alpha"][braco] + estado_segmento["beta"][braco])
        for braco in BRACOS
    }

    melhor_braco = max(taxas_estimadas, key=taxas_estimadas.get)

    return RecomendacaoResponse(
        segmento=segmento,
        oferta_recomendada=melhor_braco,
        taxa_conversao_estimada=round(taxas_estimadas[melhor_braco], 4)
    )


@app.get("/")
def root():
    return {"status": "ok", "mensagem": "API de recomendação de oferta - Datathon Grupo 43"}