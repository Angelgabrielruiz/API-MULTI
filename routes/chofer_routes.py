from fastapi import APIRouter, HTTPException
from model.chofer_connection import ChoferConnection
from schema.chofer_schema import ChoferSchema

router = APIRouter()
conn = ChoferConnection()

@router.get("/api/chofer/")
def get_all():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@router.get("/api/chofer/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    if data:
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        return dictionary
    raise HTTPException(status_code=404, detail="Chofer no encontrado")

@router.post("/api/chofer/post")
def insert(chofer_data: ChoferSchema):
    data = chofer_data.dict()
    data.pop("id")
    conn.write(data)
    return {"message": "Chofer agregado correctamente", "data": data}

@router.put("/api/chofer/update/{id}")
def update(chofer_data: ChoferSchema, id: str):
    data = chofer_data.dict()
    data["id"] = id
    conn.update(data)
    return {"message": "Chofer editado correctamente", "data": data}

@router.delete("/api/chofer/delete/{id}")
def delete(id: str):
    conn.delete(id)
    return {"message": "Chofer eliminado correctamente"}

@router.get("/api/chofer/{id}/reservas")
def get_reservas(id: str):
    data = conn.get_reservas_by_chofer(id)
    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron reservas para este chofer")
    reservas = []
    for reserva in data:
        reservas.append({
            "reserva_id": reserva[0],
            "pasajero": reserva[1],
            "origen": reserva[2],
            "destino": reserva[3],
        })
    return reservas
