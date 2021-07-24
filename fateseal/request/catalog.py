from .abc import RequestType

class CardNames(RequestType):
    """Returns a Catalog of all card names"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/card-names"

class ArtistNames(RequestType):
    """Returns a Catalog of all artist names"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/artist-names"

class WordBank(RequestType):
    """Returns a Catalog of the word bank """
    def __init__(self) -> None:
        self.endpoint = "/catalog/word-bank"

class CreatureTypes(RequestType):
    """Returns a Catalog of all creature types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/creature-types"

class PlaneswalkerTypes(RequestType):
    """Returns a Catalog of all planeswalker types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/planeswalker-types"

class LandTypes(RequestType):
    """Returns a Catalog of all land types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/land-types"

class ArtifactTypes(RequestType):
    """Returns a Catalog of all artifact types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/artifact-types"

class EnchantmentTypes(RequestType):
    """Returns a Catalog of all enchantment types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/enchantment-types"

class SpellTypes(RequestType):
    """Returns a Catalog of all spell types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/spell-types"

class Powers(RequestType):
    """Returns a Catalog of all valid powers"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/powers"

class Toughnesses(RequestType):
    """Returns a Catalog of all valid toughnesses"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/toughnesses"

class Loyalties(RequestType):
    """Returns a Catalog of all loyalties"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/loyalties"

class Watermarks(RequestType):
    """Returns a Catalog of all watermarks"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/watermarks"

class KeywordAbilities(RequestType):
    """Returns a Catalog of all keyword abilities"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/keyword-abilities"

class KeywordActions(RequestType):
    """Returns a Catalog of all keyword actions"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/keyword-actions"

class AbilityWords(RequestType):
    """Returns a Catalog of all ability words"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/ability-words"
