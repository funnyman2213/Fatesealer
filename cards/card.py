from pydantic import BaseModel
from uuid import UUID
from typing import Literal, Optional, List

MANACOLOR = Literal['W', "U", "B", "R", "G"]
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
    png: Optional[str] = None
    border_crop: Optional[str] = None
    art_crop: Optional[str] = None
    large: Optional[str] = None
    normal: Optional[str] = None
    small: Optional[str] = None

class Prices(BaseModel):
    usd: Optional[str] = None
    usd_foil: Optional[str] = None
    eur: Optional[str] = None
    eur_foil: Optional[str] = None
    tix: Optional[str] = None

class PurchaseUris(BaseModel):
    tcgplayer: Optional[str] = None
    cardmarket: Optional[str] = None
    cardhoarder: Optional[str] = None

class RelatedUris(BaseModel):
    gatherer: Optional[str] = None
    tcgplayer_infinite_articles: Optional[str] = None
    tcgplayer_infinite_decks: Optional[str] = None
    edhrec: Optional[str] = None
    mtgtop8: Optional[str] = None

class Preview(BaseModel):
    previewed_at: Optional[str] = None
    source_uri: Optional[str] = None
    source: Optional[str] = None

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

    artist: Optional[str] = None
    artist_ids: Optional[List[str]] = None
    color_indicator: Optional[List[MANACOLOR]] = None
    colors: Optional[List[MANACOLOR]] = None
    flavor_text: Optional[str] = None
    illustration_id: Optional[UUID] = None #UUID
    image_uris: Optional[ImageUris] = None 
    loyalty: Optional[str] = None
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    printed_name: Optional[str] = None
    printed_text: Optional[str] = None
    printed_type_line: Optional[str] = None
    toughness: Optional[str] = None
    watermark: Optional[str] = None

class Card(BaseModel):
    # Core Atributes
    id: str #uuid
    lang: str
    object: str
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
    arena_id: Optional[int] = None
    mtgo_id: Optional[int] = None
    mtgo_foil_id: Optional[int] = None
    multiverse_ids: Optional[List[int]] = None
    tcgplayer_id: Optional[int] = None
    cardmarket_id: Optional[int] = None

    # Gameplay Optionals
    all_parts: Optional[List[RelatedCards]] = None
    card_faces: Optional[List[CardFace]] = None
    color_idicator: Optional[List[MANACOLOR]] = None
    colors: Optional[List[MANACOLOR]] = None
    edhrec_rank: Optional[int] = None
    hand_modfier: Optional[str] = None
    life_modifier: Optional[str] = None
    loyalty: Optional[str] = None
    mana_cost: Optional[str] = None
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    produced_mana: Optional[List[MANACOLOR]] = None
    toughness: Optional[str] = None

    # Print Optionals
    artist: Optional[str] = None
    artist_ids: Optional[List[str]] = None
    content_warning: Optional[bool] = None
    flavor_name: Optional[str] = None
    flavor_text: Optional[str] = None
    frame_effects: Optional[List[str]] = None
    illustration_id: Optional[UUID] = None #UUID
    image_uris: Optional[ImageUris] = None #URI
    printed_name: Optional[str] = None
    printed_text: Optional[str] = None
    printed_type_line: Optional[str] = None
    promo_types: Optional[List[str]] = None
    variation_of: Optional[UUID] = None #UUID
    watermark: Optional[str] = None
    preview: Optional[Preview] = None