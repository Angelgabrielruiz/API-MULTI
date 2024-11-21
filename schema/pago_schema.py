from pydantic import BaseModel
from typing import Optional

class PagoSchema(BaseModel):
    id: Optional[int]
    tarifa: int
    forma_de_pago: str
    estado: str
    pasajero_id: int
