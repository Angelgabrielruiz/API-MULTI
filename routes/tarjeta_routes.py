from fastapi import APIRouter
from model.tarjeta_connection import TarjetaConnection
from schema.tarjeta_schema import TarjetaSchema

router = APIRouter()
conn = TarjetaConnection()


@router.get("/api/tarjeta/")
def get_all():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        dictionary["num_tarjeta"] = data[2]
        dictionary["fecha_expiracion"] = data[3]
        dictionary["cvc"] = data[4]
        items.append(dictionary)
    return items


@router.get("/api/tarjeta/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    dictionary["num_tarjeta"] = data[2]
    dictionary["fecha_expiracion"] = data[3]
    dictionary["cvc"] = data[4]
    return dictionary


@router.post("/api/tarjeta/post")
def insert(tarjeta_data: TarjetaSchema):
    data = tarjeta_data.dict()
    data.pop("id")
    conn.write(data)


@router.put("/api/tarjeta/update/{id}")
def update(tarjeta_data: TarjetaSchema, id: str):
    data = tarjeta_data.dict()
    data["id"] = id
    conn.update(data)


@router.delete("/api/tarjeta/delete/{id}")
def delete(id: str):
    conn.delete(id)
