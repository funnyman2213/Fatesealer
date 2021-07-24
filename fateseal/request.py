from typing import Union
from fateseal.abc import ScryfallObject
from fateseal.bulkdata import BulkData
from fateseal.card import Card
from fateseal.catalog import Catalog
from fateseal.error import Error
from fateseal.objlist import ObjList
from fateseal.ruling import Ruling
from fateseal.set import CardSet
from fateseal.symbol import CardSymbol

from abc import ABC, abstractclassmethod

import request
import aiohttp

class RequestType(ABC):

    def get() -> ScryfallObject:
        pass #TODO: impliment get using request library

    async def async_get() -> ScryfallObject:
        pass #TODO: impliment asyncronous get using aiohttp library

