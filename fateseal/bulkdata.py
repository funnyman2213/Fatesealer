from fateseal.abc import ScryfallObject
from uuid import UUID

class BulkData(ScryfallObject):
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