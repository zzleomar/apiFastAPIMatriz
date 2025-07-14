from fastapi import APIRouter, HTTPException
from entities.requestModel import MatrizRequest
from process.matriz_traspuesta_processor import MatrizOPerationProcess
from validators.matriz_traspuesta_validator import MatrizTraspuestaValidator

router = APIRouter(prefix="/operation", tags=["matriz"])

# servicio de matrices
@router.post("/traspuesta")
async def traspuesta(request: MatrizRequest):
    validator = MatrizTraspuestaValidator()
    process = MatrizOPerationProcess()
    
    isValid, message = validator.validateMatricesInput(
        request.matriz
    )
    
    if not isValid:
        raise HTTPException(
            status_code=400, 
            detail={"message": message, "status": False}
        )
    
    result = process.processMatrices(
        request.matriz
    )
    
    return {"message": result, "status": True}