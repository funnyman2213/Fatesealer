from fateseal.abc import ScryfallObject
from typing import Optional
from uuid import UUID

class CardSet(ScryfallObject):
    id: UUID
    code: str
    name: str
    set_type: str
    card_count: int
    digital: bool
    foil_only: bool
    nonfoil_only: bool
    scryfall_uri: str #URI
    uri: str #URI
    icon_svg_uri: str #URI
    search_uri: str #URI

    mtgo_code: Optional[str] = None
    tcgplayter_id: Optional[int] = None
    released_at: Optional[str] = None
    block_code: Optional[str] = None
    block: Optional[str] = None
    parent_set_code: Optional[str] = None
    printed_size: Optional[int] = None