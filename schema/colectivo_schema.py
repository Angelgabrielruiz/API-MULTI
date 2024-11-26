from pydantic import BaseModel
from typing import Optional

class ColectivoSchema (BaseModel):
    id: Optional[int] = None
    asientos: int
    ubicacion: str
    num_serie: str
    fecha : str
    horario : str