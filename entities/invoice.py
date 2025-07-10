from pydantic import BaseModel
from typing import Optional
from .client import Client

class Invoice(BaseModel):
    id: Optional[int] = None
    client: Client
    amount: float