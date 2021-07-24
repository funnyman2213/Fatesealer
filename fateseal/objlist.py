from fateseal.abc import ScryfallObject
from fateseal.ruling import Ruling
from fateseal.bulkdata import BulkData
from fateseal.symbol import CardSymbol
from fateseal.set import CardSet
from fateseal.card import Card
from typing import Optional, List, Union

class ObjList(ScryfallObject):
    data: List[Union[Card, CardSet, Ruling, CardSymbol, BulkData]]
    has_more: bool
    next_page: Optional[str] = None
    total_cards: Optional[int] = None
    warnings: Optional[List[str]] = None