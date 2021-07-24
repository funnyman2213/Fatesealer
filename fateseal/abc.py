from abc import ABC
from pydantic import BaseModel

class ScryfallObject(BaseModel, ABC):
    object: str