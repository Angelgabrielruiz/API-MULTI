from fastapi import APIRouter
from model.reservas_connection import ReservasConnection
from schema.reservas_schema import ReservasSchema

router = APIRouter()
conn = ReservasConnection()


@router.get("/api/reservas/")
def get_all():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["estado"] = data[1]
        dictionary["fecha_reserva"] = data[2]
        dictionary["forma_pago"] = data[3]
        dictionary["monto"] = data[4]
        dictionary["pasajero_id"] = data[5]
        dictionary["cantidad"] = data[6]
        
        items.append(dictionary)
    return items


@router.get("/api/reservas/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["estado"] = data[1]
    dictionary["fecha_reserva"] = data[2]
    dictionary["forma_pago"] = data[3]
    dictionary["monto"] = data[4]
    dictionary["pasajero_id"] = data[5]
    dictionary["cantidad"] = data[6]
    return dictionary


@router.post("/api/reservas/post")
def insert(reservas_data: ReservasSchema):
    data = reservas_data.dict()
    data.pop("id")
    conn.write(data)


@router.put("/api/reservas/update/{id}")
def update(reservas_data: ReservasSchema, id: str):
    data = reservas_data.dict()
    data["id"] = id
    conn.update(data)


@router.delete("/api/reservas/delete/{id}")
def delete(id: str):
    conn.delete(id)
