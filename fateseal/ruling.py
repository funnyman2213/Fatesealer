from fateseal.abc import ScryfallObject
from uuid import UUID

class Ruling(ScryfallObject):
    oracle_id: UUID
    source: str
    published_at: str
    comment: str