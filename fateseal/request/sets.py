from uuid import UUID
from .abc import RequestType

class All(RequestType):
    """Returns all Sets"""
    def __init__(self) -> None:
        self.endpoint = "/sets"

class ByCode(RequestType):
    """Returns Set with specified code"""
    def __init__(self, code:str) -> None:
        self.endpoint = f"/sets/{code}"

class TCGPlayerID(RequestType):
    """Returns Set with TCGPlayer ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/sets/tcgplayer/{id}"

class ByID(RequestType):
    """Returns Set with Scryfall UUID"""
    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/sets/{id}"