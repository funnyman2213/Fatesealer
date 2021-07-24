from fateseal.abc import ScryfallObject
from fateseal.card import MANACOLOR
from typing import List, Optional

class CardSymbol(ScryfallObject):
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