from pydantic import BaseModel
from typing import Optional


class PasajerosSchema(BaseModel):
    id: Optional[int] = None
    name: str
    origen: str
    destino: str
    colectivo_id: int
    chofer_id: int
