from fastapi import APIRouter, HTTPException
from model.pasajeros_connection import PasajerosConnection
from schema.pasajeros_schema import PasajerosSchema

router = APIRouter()
conn = PasajerosConnection()


@router.get("/api/pasajeros/")
def get_all():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["origen"] = data[2]
        dictionary["destino"] = data[3]
        dictionary["colectivo_id"] = data[4]
        dictionary["chofer_id"] = data[5]
        items.append(dictionary)
    return items


@router.get("/api/pasajeros/one/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["origen"] = data[2]
    dictionary["destino"] = data[3]
    dictionary["colectivo_id"] = data[4]
    dictionary["chofer_id"] = data[5]
    return dictionary


@router.post("/api/pasajeros/post")
def insert(pasajero_data: PasajerosSchema):
    data = pasajero_data.dict()
    data.pop("id")
    conn.write(data)
    return {"message": "Pasajero agregado correctamente", "data": data}


@router.put("/api/pasajeros/update/{id}")
def update(pasajero_data: PasajerosSchema, id: str):
    data = pasajero_data.dict()
    data["id"] = id
    conn.update(data)
    return {"message": "Pasajero editado correctamente", "data": data}


@router.delete("/api/pasajeros/delete/{id}")
def delete(id: str):
    conn.delete(id)


@router.get("/api/pasajeros/last")
def get_last():
    dictionary = {}
    data = conn.read_last()
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["origen"] = data[2]
    dictionary["destino"] = data[3]
    dictionary["colectivo_id"] = data[4]
    dictionary["chofer_id"] = data[5]
    return dictionary


@router.get("/api/pasajeros/colectivo/{id}")
def get_colectivo(id: str):
    data = conn.get_colectivo_by_pasajero(id)
    if not data:
        raise HTTPException(status_code=404, detail="Colectivo no encontrado para este pasajero")
    dictionary = {
        "id": data[0],
        "asientos": data[1],
        "origen": data[2],
        "destino": data[3],
        "colectivo_id": data[4],
        "chofer_id": data[5],
    }
    return dictionary
