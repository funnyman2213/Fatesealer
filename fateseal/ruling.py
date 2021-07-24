from pydantic import BaseModel
from uuid import UUID

class Ruling(BaseModel):
    object: str
    oracle_id: UUID
    source: str
    published_at: str
    comment: str