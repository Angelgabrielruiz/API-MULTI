from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.colectivo_routes import router as colectivo_router
from routes.chofer_routes import router as chofer_router
from routes.pago_routes import router as pago_router
from routes.pasajeros_routes import router as pasajeros_router
from routes.reservas_routes import router as reservas_router
from routes.tarjeta_routes import router as tarjeta_router

app = FastAPI()


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

@app.get("/")
def root():
    return {"message": "Bienvenido a la API"}
