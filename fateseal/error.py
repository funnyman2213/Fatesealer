from fateseal.abc import ScryfallObject
from typing import List, Optional

class Error(ScryfallObject):
    code: str
    status: int
    details: str
    type: Optional[str]
    warnings: Optional[List[str]]