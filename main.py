# main.py
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any
from dotenv import load_dotenv
from matrix_validator import MatrixValidator
from matrix_processor import MatrixProcessor

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

PORT = int(os.getenv("PORT", 8000))  # Default 8000, no 8002

class MatrixRequest(BaseModel):
    matrix1: List[List[int]]
    matrix2: List[List[Any]]
    i: int
    j: int

@app.get("/")
async def getHealthCheck():
    return {"message": "API is running"}

@app.get("/health")  # Endpoint adicional para monitoreo
async def getHealth():
    return {"status": "healthy"}

@app.post("/matriz")
async def processMatrices(request: MatrixRequest):
    validator = MatrixValidator()
    processor = MatrixProcessor()
    
    is_valid, message = validator.validateMatricesInput(
        request.matrix1, request.matrix2, request.i, request.j
    )
    
    if not is_valid:
        raise HTTPException(
            status_code=400, 
            detail={"message": message, "status": False}
        )
    
    result = processor.processMatrices(
        request.matrix1, request.matrix2, request.i, request.j
    )
    
    return {"message": result, "status": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)