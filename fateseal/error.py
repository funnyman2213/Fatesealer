from fateseal.abc import ScryfallObject
from typing import List, Optional

class Error(ScryfallObject):
    code: str
    status: int
    details: str
    type: Optional[str] = None
    warnings: Optional[List[str]] = None