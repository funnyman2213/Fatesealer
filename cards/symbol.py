from cards.card import MANACOLOR
from typing import List, Optional
from pydantic import BaseModel

class CardSymbol(BaseModel):
    object: str
    english: str
    transposable: bool
    represents_mana: bool
    appears_in_mana_costs: bool
    funny: bool
    colors: List[MANACOLOR]

    loose_variant: Optional[str]
    cmc: Optional[float]
    gatherer_alternatives: Optional[str]
    svg_uri: Optional[str] #URI