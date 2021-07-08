import asyncio
import re
from functools import lru_cache

import aiohttp
import discord

from utils import cacheable

COLOUR = discord.Colour(0x8b23b8)

@lru_cache(maxsize=300)
@cacheable
async def getRequest(url, **kwargs):
    from main import client
    await asyncio.sleep(0.1)
    async with aiohttp.ClientSession(loop=client.loop) as session:
        response = await session.get(url, **kwargs)
        return await response.json()

async def getCardByName(name: str) -> list[discord.Embed]:
    card = await getRequest(url='http://api.scryfall.com/cards/named?', params={'fuzzy':name})
    messages: list[discord.Embed] = list()

    if card['object'] == 'error':
        return list(discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', card['details']))
        ))
    
    if 'card_faces' in card:
        for entry in card['card_faces']:
            message = discord.Embed(
                title="**{}**".format(entry['name']),
                url=card['scryfall_uri'],
                color=COLOUR
            )
            message.set_image(url=entry['image_uris']['normal'])
            messages.append(message)
        return messages
    
    message = discord.Embed(
        title="**{}**".format(card['name']),
        url=card['scryfall_uri'],
        color=COLOUR
    )

    message.set_image(url=card['image_uris']['normal'])
    messages.append(message)
    return messages
