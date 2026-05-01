from fastapi import FastAPI
from app.schemas import FormulationRequest
from app.services import generate_formula

app = FastAPI(
    title="Glow & Gossamer Med Spa API",
    version="1.0.0",
    description="Custom Bespoke Botanical Serum Formulation Engine"
)


@app.get("/")
def root():
    return {"message": "Glow & Gossamer API Running"}


@app.post("/formulate")
def formulate(payload: FormulationRequest):
    formula = generate_formula(
        payload.skin_type,
        payload.primary_concern,
        payload.intensity
    )

    return {
        "skin_type": payload.skin_type,
        "primary_concern": payload.primary_concern,
        "intensity": payload.intensity,
        "formula": formula
    }