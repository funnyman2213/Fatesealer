from cards.ruling import Ruling
from cards.bulkdata import BulkData
from cards.symbol import CardSymbol
from cards.set import CardSet
from cards.card import Card
from pydantic import BaseModel
from typing import Optional, List, Union

class ObjList(BaseModel):
    data: List[Union[Card, CardSet, Ruling, CardSymbol, BulkData]]
    has_more: bool
    next_page: Optional[str] = None
    total_cards: Optional[int] = None
    warnings: Optional[List[str]] = None