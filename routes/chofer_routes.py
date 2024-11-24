from fastapi import APIRouter, Depends, HTTPException
from model.chofer_connection import ChoferConnection
from schema.chofer_schema import ChoferSchema
from jose import jwt

router = APIRouter()
conn = ChoferConnection()

SECRET_KEY = "secreto-amor"  # Asegúrate de que este coincide con el de main.py
ALGORITHM = "HS256"

# Función para decodificar el token
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

@router.get("/api/chofer/")
def get_all(token: str = Depends(decode_token)):
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@router.get("/api/chofer/{id}")
def get_one(id: str, token: str = Depends(decode_token)):
    dictionary = {}
    data = conn.read_one(id)
    if data:
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        return dictionary
    raise HTTPException(status_code=404, detail="Chofer no encontrado")

@router.post("/api/chofer/post")
def insert(chofer_data: ChoferSchema, token: str = Depends(decode_token)):
    data = chofer_data.dict()
    data.pop("id")
    conn.write(data)
    return {"message": "Chofer agregado correctamente", "data": data}

@router.put("/api/chofer/update/{id}")
def update(chofer_data: ChoferSchema, id: str, token: str = Depends(decode_token)):
    data = chofer_data.dict()
    data["id"] = id
    conn.update(data)
    return {"message": "chofer editado correctamente", "data": data}

@router.delete("/api/chofer/delete/{id}")
def delete(id: str, token: str = Depends(decode_token)):
    conn.delete(id)
    return {"message": "Chofer eliminado correctamente"}
