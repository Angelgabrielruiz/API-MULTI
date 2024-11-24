from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.colectivo_routes import router as colectivo_router
from routes.chofer_routes import router as chofer_router
from routes.pago_routes import router as pago_router
from routes.pasajeros_routes import router as pasajeros_router
from routes.reservas_routes import router as reservas_router
from routes.tarjeta_routes import router as tarjeta_router
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt

app = FastAPI()
oauth2_schema = OAuth2PasswordBearer (tokenUrl="token")

users = {
    "chame": {"username": "chame", "email": "chame@gmail.com", "password": "1234"}
}

def encode_token(payload: dict) -> str:
    token = jwt
    return "pruebita"

def decode_token(token: Annotated[str, Depends(oauth2_schema)]) -> dict:
    return users.get("chame")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


app.include_router(colectivo_router)
app.include_router(chofer_router)
app.include_router(pago_router)
app.include_router(pasajeros_router)
app.include_router(reservas_router)
app.include_router(tarjeta_router)

@app.post("/token")
def root(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect Username")
    
    token = encode_token({"username": user["username"], "email": user["email"]})
    
    return { "access_token":token }

@app.get ("/users/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user