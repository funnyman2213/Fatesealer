from typing import List
from pydantic import BaseModel

class Catalog(BaseModel):
    object: str
    uri: str #URI
    total_values: int
    data: List[str]