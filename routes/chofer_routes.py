from fastapi import APIRouter
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
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary


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


@router.delete("/api/chofer/delete/{id}")
def delete(id: str):
    conn.delete(id)
