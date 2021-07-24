from .abc import RequestType

class All(RequestType):
    """Returns all valid Symbols"""
    def __init__(self) -> None:
        self.endpoint = "/symbology"

class ParseMana(RequestType):
    """Returns information about the requested mana string"""
    def __init__(self, query:str) -> None:
        self.endpoint = "/symbology/parse-mana"
        self._set_paramaters([
            ('cost', query)
        ])