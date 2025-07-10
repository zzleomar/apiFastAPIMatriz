from pydantic import BaseModel
from typing import Optional

class Client(BaseModel):
    id: Optional[int] = None
    fullName: str
    document: str