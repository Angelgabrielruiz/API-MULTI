from pydantic import BaseModel
from typing import Optional

class ChoferSchema(BaseModel):
    id: Optional[int]
    nombre: str
