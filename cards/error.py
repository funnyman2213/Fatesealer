from typing import List, Optional
from pydantic import BaseModel

class Error(BaseModel):
    object: str
    code: str
    status: int
    details: str
    type: Optional[str] = None
    warnings: Optional[List[str]] = None