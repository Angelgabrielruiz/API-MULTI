from fastapi import APIRouter
from model.colectivo_connection import ColectivoConnection
from schema.colectivo_schema import ColectivoSchema

router = APIRouter()
conn = ColectivoConnection()

@router.get("/api/colectivo/")
def get_all():
    items = [] 
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["asientos"] = data[1]
        dictionary["ubicacion"] = data[2]
        dictionary["num_ser"] = data[3]
        dictionary["fecha"] = data[4]
        dictionary["horario"] = data[5]
        items.append(dictionary)
    return items


@router.get("/api/colectivo/{id}")
def get_one(id: str):
    dictionary = {}
    data = conn.read_one(id)
    if data:  
        dictionary["id"] = data[0]
        dictionary["asientos"] = data[1]
        dictionary["ubicacion"] = data[2]
        dictionary["num_ser"] = data[3]
        dictionary["fecha"] = data[4]
        dictionary["horario"] = data[5]
        return dictionary
    return {"error": "Colectivo no encontrado"}

@router.post("/api/colectivo/post")
def insert(colectivo_data: ColectivoSchema):
    data = colectivo_data.dict()
    data.pop("id") 
    conn.write(data)
    return {"message": "Colectivo agregado exitosamente"}

@router.put("/api/colectivo/update/{id}")
def update(colectivo_data: ColectivoSchema, id: str):
    data = colectivo_data.dict()
    data["id"] = id  
    conn.update(data)
    return {"message": "Colectivo actualizado exitosamente"}

@router.delete("/api/colectivo/delete/{id}")
def delete(id: str):
    conn.delete(id)
    return {"message": "Colectivo eliminado exitosamente"}
