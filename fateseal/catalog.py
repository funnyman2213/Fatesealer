from fateseal.abc import ScryfallObject
from typing import List

class Catalog(ScryfallObject):
    uri: str #URI
    total_values: int
    data: List[str]