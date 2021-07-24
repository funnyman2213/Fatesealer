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

    mtgo_code: Optional[str]
    tcgplayter_id: Optional[int]
    released_at: Optional[str]
    block_code: Optional[str]
    block: Optional[str]
    parent_set_code: Optional[str]
    printed_size: Optional[int]