from pydantic import BaseModel
from typing import Optional

class TarjetaSchema(BaseModel):
    id: Optional[int]
    nombre: str
    num_tarjeta: int
    fecha_expiracion: str
    cvc: int
