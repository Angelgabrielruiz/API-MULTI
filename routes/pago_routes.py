from fastapi import APIRouter
from model.pago_connection import PagoConnection
from schema.pago_schema import PagoSchema

router = APIRouter()
conn = PagoConnection()


@router.get("/api/pago/")
def get_all():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["tarifa"] = data[1]
        dictionary["forma_de_pago"] = data[2]
        dictionary["estado"] = data[3]
        dictionary["pasajero_id"] = data[4]
        items.append(dictionary)
    return items


@router.get("/api/pago/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["tarifa"] = data[1]
    dictionary["forma_de_pago"] = data[2]
    dictionary["estado"] = data[3]
    dictionary["pasajero_id"] = data[4]
    return dictionary


@router.post("/api/pago/post")
def insert(pago_data: PagoSchema):
    data = pago_data.dict()
    data.pop("id")
    conn.write(data)
    return {"message": "Pago agregado correctamente", "data": data}


@router.put("/api/pago/update/{id}")
def update(pago_data: PagoSchema, id: str):
    data = pago_data.dict()
    data["id"] = id
    conn.update(data)
    return {"message": "Pago editado correctamente", "data": data}


@router.delete("/api/pago/delete/{id}")
def delete(id: str):
    conn.delete(id)
