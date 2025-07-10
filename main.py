# main.py
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.invoice_routes import router as invoiceRouter
from routes.matriz_routes import router as matrizRouter

load_dotenv()

app = FastAPI(title="Matrix API", version="1.0.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiarás esto después por tu dominio de GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PORT = int(os.getenv("PORT", 8000))

# Incluir routers
app.include_router(invoiceRouter)
app.include_router(matrizRouter)

@app.get("/")
async def getHealthCheck():
    return {"message": "API is running"}

@app.get("/health")  # Endpoint adicional para monitoreo
async def getHealth():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)