from pydantic import BaseModel
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_class: str
    confidence: float
    all_predictions: Dict[str, float]
    
class HealthResponse(BaseModel):
    status: str
    message: str
