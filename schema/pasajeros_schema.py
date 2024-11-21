from pydantic import BaseModel
from typing import Optional
from datetime import date

class PasajerosSchema(BaseModel):
    id: Optional[int]
    name: str
    origen: str
    destino: str
    fechadeviaje: date
    colectivo_id: int
    chofer_id: int
