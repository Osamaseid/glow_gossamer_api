from pydantic import BaseModel, Field
from typing import Literal


class FormulationRequest(BaseModel):
    skin_type: Literal["Dry", "Oily", "Sensitive", "Combination"]
    primary_concern: Literal["Aging", "Acne", "Redness", "Dehydration"]
    intensity: int = Field(..., ge=1, le=3)


class FormulationResponse(BaseModel):
    skin_type: str
    primary_concern: str
    formula: dict