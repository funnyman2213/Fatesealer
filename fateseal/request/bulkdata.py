from typing import Literal

from .abc import RequestType

class All(RequestType):
    """Returns a List of all Bulk Data entries"""
    def __init__(self) -> None:
        self.endpoint = "/bulk-data"

class ByID(RequestType):
    """Returns a Bulk Data entry based on ID"""
    def __init__(self, id: str) -> None:
        self.endpoint = "/bulk-data/{}".format(id)

class ByType(RequestType):
    """Returns a Bulk Data entry based on Type"""
    def __init__(self, type: Literal["oracle_cards", "unique_artwork", "default_cards", "all_cards", "rulings"]) -> None:
        self.endpoint = "/bulk-data/{}".format(type)