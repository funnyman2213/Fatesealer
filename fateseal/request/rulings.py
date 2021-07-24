from uuid import UUID
from .abc import RequestType

# TODO: FIX THIS FILE. THIS IS BAD IMPLIMENTATION
# MUTATES CARD REQUESTS TO APPEND /RULINGS

class Multiverse(RequestType):
    """Returns a List of Rulings for a Card of Multiverse ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/multiverse/{id}/rulings"

class Mtgo(RequestType):
    """Returns a List of Rulings for a Card of MTGO ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/mtgo/{id}/rulings"

class Arena(RequestType):
    """Returns a List of Rulings for a Card of Arena ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/arena/{id}/rulings"

class ByCode(RequestType):
    """Returns a List of Rulings for a Card in set with collecter number"""
    def __init__(self, code:str, number:int) -> None:
        self.endpoint = f"/cards/{code}/{number}/rulings"

class ByID(RequestType):
    """Returns a List of Rulings for a Card of Scryfall UUID"""
    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/cards/{id}/rulings"