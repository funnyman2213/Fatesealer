from pydantic import BaseModel
from uuid import UUID

class BulkData(BaseModel):
    object: str
    id: UUID
    uri: str
    type: str
    name: str
    description: str
    download_uri: str
    update_at: str # DATE
    compressed_size: int
    content_type: str
    content_encoding: str