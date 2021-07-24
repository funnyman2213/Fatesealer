from .abc import RequestType

# TODO: FIX THIS FILE. THIS IS BAD IMPLIMENTATION
# MUTATES CARD REQUESTS TO APPEND /RULINGS

class Multiverse(RequestType):
    pass

class Mtgo(RequestType):
    pass

class Arena(RequestType):
    pass

class ByCode(RequestType):
    pass

class ByID(RequestType):
    pass