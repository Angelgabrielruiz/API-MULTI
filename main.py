from fastapi import FastAPI
from routes.colectivo_routes import router as colectivo_router
from routes.chofer_routes import router as chofer_router
from routes.pago_routes import router as pago_router
from routes.pasajeros_routes import router as pasajeros_router
from routes.reservas_routes import router as reservas_router
from routes.tarjeta_routes import router as tarjeta_router

app = FastAPI()

# Incluir las rutas de colectivo
app.include_router(colectivo_router)
app.include_router(chofer_router)
app.include_router(pago_router)
app.include_router(pasajeros_router)
app.include_router(reservas_router)
app.include_router(tarjeta_router)

@app.get("/")
def root():
    colectivo_router
    chofer_router
    pago_router
    pasajeros_router
    reservas_router
    tarjeta_router
    return {"message": "Bienvenido a la API"}
