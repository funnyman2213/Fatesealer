from .abc import RequestType

class Search(RequestType):
    pass

class Named(RequestType):
    pass

class Autocomplete(RequestType):
    pass

class Random(RequestType):
    def __init__(self):
        self.endpoint = "/cards/random"

class Collection(RequestType):
    #TODO: work on this. this one will be an interesting build
    pass 

class BySetCode(RequestType):
    pass

class Multiverse(RequestType):
    pass

class Mtgo(RequestType):
    pass

class Arena(RequestType):
    pass

class TCGPlayer(RequestType):
    pass

class CardMarket(RequestType):
    pass

class ByID(RequestType):
    pass