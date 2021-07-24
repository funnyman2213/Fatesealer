from fateseal.symbol import CardSymbol
from fateseal.set import CardSet
from fateseal.ruling import Ruling
from fateseal.objlist import ObjList
from fateseal.error import Error
from fateseal.catalog import Catalog
from fateseal.bulkdata import BulkData
from fateseal.card import Card
from typing import Dict, Optional
from fateseal.abc import ScryfallObject

from abc import ABC

import requests
import aiohttp

class RequestType(ABC):
    base_uri = "https://api.scryfall.com"
    endpoint: str
    params: Optional[Dict[str, str]] = None

    def _interpret(self, object:str) -> ScryfallObject:
        objects = {
            "bulk_data": BulkData,
            "card": Card,
            "catalog": Catalog,
            "error": Error,
            "list": ObjList,
            "ruling": Ruling,
            "set": CardSet,
            "card_symbol": CardSymbol
        }
        if object in objects:
            return objects[object]

    def get(self) -> ScryfallObject:
        r = requests.get(self.base_uri + self.endpoint, params=self.params)
        return self._interpret(r.json()["object"]).parse_raw(r.text)

    async def async_get(self) -> ScryfallObject:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_uri + self.endpoint, params=self.params) as response:   
                responseJson = await response.json()
                objectType = self._interpret(responseJson['object'])
                return objectType.parse_raw(await response.text())

