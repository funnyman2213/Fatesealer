from fateseal.card import MANACOLOR
from typing import List
from fateseal.abc import ScryfallObject

class ManaCost(ScryfallObject):
    cost: str
    cmc: float
    colors: List[MANACOLOR]
    colorless: bool
    monocolored: bool
    multicolored: bool