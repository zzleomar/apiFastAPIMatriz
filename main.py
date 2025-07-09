# main.py
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from matrix_validator import MatrixValidator
from matrix_processor import MatrixProcessor
from typing import Any
load_dotenv()

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los headers
)

PORT = int(os.getenv("PORT", 8000))


class MatrixRequest(BaseModel):
    matrix1: List[List[int]]
    matrix2: List[List[Any]]
    i: int
    j: int


@app.get("/")
async def getHealthCheck():
    return {"message": "API is running"}


@app.post("/matriz")
async def processMatrices(request: MatrixRequest):
    validator = MatrixValidator()
    processor = MatrixProcessor()
    
    is_valid, message = validator.validateMatricesInput(request.matrix1, request.matrix2, request.i, request.j)
    
    if not is_valid:
        raise HTTPException(status_code=400, detail={"message": message, "status": False})
    
    result = processor.processMatrices(request.matrix1, request.matrix2, request.i, request.j)
    
    return {"message": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)