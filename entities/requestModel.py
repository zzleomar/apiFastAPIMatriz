from pydantic import BaseModel
from typing import List, Any, Optional
from entities.client import Client

class InvoiceRequest(BaseModel):
    clientId: Optional[int] = None
    clientData: Optional[Client] = None
    amount: float

class MatrixRequest(BaseModel):
    matrix1: List[List[int]]
    matrix2: List[List[Any]]
    i: int
    j: int

class MatrizRequest(BaseModel):
    matriz: List[List[Any]]