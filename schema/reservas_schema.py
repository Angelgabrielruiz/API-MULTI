from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReservasSchema(BaseModel):
    id: Optional[int] = None
    fecha_reserva: date
    forma_pago: str
    monto: int
    pasajero_id: int
    cantidad : int
