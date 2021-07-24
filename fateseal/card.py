from fateseal.abc import ScryfallObject
from pydantic import BaseModel
from uuid import UUID
from typing import Literal, Optional, List

MANACOLOR = Literal['W', "U", "B", "R", "G", "C"]
Legality = Literal["legal","not_legal","restricted","banned"]

class Legalities(BaseModel):
    standard: Legality
    future: Legality
    historic: Legality
    gladiator: Legality
    pioneer: Legality
    modern: Legality
    legacy: Legality
    pauper: Legality
    vintage: Legality
    penny: Legality
    commander: Legality
    brawl: Legality
    duel: Legality
    oldschool: Legality
    premodern: Legality

class ImageUris(BaseModel):
    png: Optional[str]
    border_crop: Optional[str]
    art_crop: Optional[str]
    large: Optional[str]
    normal: Optional[str]
    small: Optional[str]

class Prices(BaseModel):
    usd: Optional[str]
    usd_foil: Optional[str]
    eur: Optional[str]
    eur_foil: Optional[str]
    tix: Optional[str]

class PurchaseUris(BaseModel):
    tcgplayer: Optional[str]
    cardmarket: Optional[str]
    cardhoarder: Optional[str]

class RelatedUris(BaseModel):
    gatherer: Optional[str]
    tcgplayer_infinite_articles: Optional[str]
    tcgplayer_infinite_decks: Optional[str]
    edhrec: Optional[str]
    mtgtop8: Optional[str]

class Preview(BaseModel):
    previewed_at: Optional[str]
    source_uri: Optional[str]
    source: Optional[str]

class RelatedCards(BaseModel):
    id: UUID #UUID
    object: str
    component: str
    name: str
    type_line: str
    uri: str #URI

class CardFace(BaseModel):
    mana_cost: str
    name: str
    object: str
    type_line: str

    artist: Optional[str]
    artist_ids: Optional[List[str]]
    color_indicator: Optional[List[MANACOLOR]]
    colors: Optional[List[MANACOLOR]]
    flavor_text: Optional[str]
    illustration_id: Optional[UUID] #UUID
    image_uris: Optional[ImageUris] 
    loyalty: Optional[str]
    oracle_text: Optional[str]
    power: Optional[str]
    printed_name: Optional[str]
    printed_text: Optional[str]
    printed_type_line: Optional[str]
    toughness: Optional[str]
    watermark: Optional[str]

class Card(ScryfallObject):
    # Core Atributes
    id: str #uuid
    lang: str
    oracle_id: UUID #UUID
    prints_search_uri: str #uri
    rulings_uri: str #uri
    scryfall_uri: str #uri
    uri: str # uri
    
    # Gameplay Atributes
    cmc: float
    color_identity: List[MANACOLOR]
    foil: bool
    keywords: List[str]
    layout: str
    legalities: Legalities
    name: str
    nonfoil: bool
    oversized: bool
    reserved: bool
    type_line: str

    # Print Atributes
    booster: bool
    border_color: str
    card_back_id: UUID #UUID
    collector_number: str
    digital: bool
    frame: str
    full_art: bool
    games: List[str]
    highres_image: bool
    image_status: str
    prices: Prices
    promo: bool
    purchase_uris: PurchaseUris
    rarity: str
    related_uris: RelatedUris
    released_at: str #DATE
    reprint: bool
    scryfall_set_uri: str #URI
    set_name: str 
    set_search_uri: str #URI
    set_type: str
    set_uri: str #URI
    set: str
    set_id: str
    story_spotlight: bool
    textless: bool
    variation: bool

    # Core Optionals
    arena_id: Optional[int]
    mtgo_id: Optional[int]
    mtgo_foil_id: Optional[int]
    multiverse_ids: Optional[List[int]]
    tcgplayer_id: Optional[int]
    cardmarket_id: Optional[int]

    # Gameplay Optionals
    all_parts: Optional[List[RelatedCards]]
    card_faces: Optional[List[CardFace]]
    color_idicator: Optional[List[MANACOLOR]]
    colors: Optional[List[MANACOLOR]]
    edhrec_rank: Optional[int]
    hand_modfier: Optional[str]
    life_modifier: Optional[str]
    loyalty: Optional[str]
    mana_cost: Optional[str]
    oracle_text: Optional[str]
    power: Optional[str]
    produced_mana: Optional[List[MANACOLOR]]
    toughness: Optional[str]

    # Print Optionals
    artist: Optional[str]
    artist_ids: Optional[List[str]]
    content_warning: Optional[bool]
    flavor_name: Optional[str]
    flavor_text: Optional[str]
    frame_effects: Optional[List[str]]
    illustration_id: Optional[UUID] #UUID
    image_uris: Optional[ImageUris] #URI
    printed_name: Optional[str]
    printed_text: Optional[str]
    printed_type_line: Optional[str]
    promo_types: Optional[List[str]]
    variation_of: Optional[UUID] #UUID
    watermark: Optional[str]
    preview: Optional[Preview]