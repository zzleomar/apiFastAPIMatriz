from fastapi import APIRouter, HTTPException
from entities.requestModel import MatrixRequest
from validators.matriz_validator import MatrizValidator
from process.matriz_processor import MatrizProcessor

router = APIRouter(prefix="/matriz", tags=["matriz"])

# servicio de matrices
@router.post("/")
async def processMatrices(request: MatrixRequest):
    validator = MatrizValidator()
    processor = MatrizProcessor()
    
    isValid, message = validator.validateMatricesInput(
        request.matrix1, request.matrix2, request.i, request.j
    )
    
    if not isValid:
        raise HTTPException(
            status_code=400, 
            detail={"message": message, "status": False}
        )
    
    result = processor.processMatrices(
        request.matrix1, request.matrix2, request.i, request.j
    )
    
    return {"message": result, "status": True}