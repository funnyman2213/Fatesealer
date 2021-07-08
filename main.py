import os
import re
import asyncio
import re

import aiohttp
import discord
import urllib.parse as urlparse

import discord

client = discord.Client()

@client.event
async def on_ready():
    print("loggin in as {0.user}".format(client))

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if "[" in message.content and "]" in message.content:
        groups = re.findall(r'\B\[([^\[\]]*)\]\B', message.content)
        if groups:
            for group in groups:
                async with message.channel.typing():
                    if group.startswith('!s '):
                        cards = await getCardFromSearch(group[3:])
                        for card in cards:
                            await message.channel.send(embed=card)
                    else:
                        cards = await getCardByName(group)
                        for card in cards:
                            await message.channel.send(embed=card)

COLOUR = discord.Colour(0x8b23b8)

async def getRequest(url, **kwargs):
    await asyncio.sleep(0.1)
    async with aiohttp.ClientSession(loop=client.loop) as session:
        response = await session.get(url, **kwargs)
        return await response.json()

async def getCardByName(name: str) -> list[discord.Embed]:
    card = await getRequest(url='http://api.scryfall.com/cards/named?', params={'fuzzy':name})
    messages: list[discord.Embed] = list()

    if card['object'] == 'error':
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', card['details']))
        ),]
    
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

async def getCardFromSearch(search: str) -> list[discord.Embed]:
    cards = await getRequest(url='http://api.scryfall.com/cards/search?', params={'q':search})
    messages: list[discord.Embed]= list()
    
    # returns if error ie. no results found
    if cards['object'] == 'error':
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', cards['details']))
        ),]

    # returns the first result of the search
    firstResult = cards['data'][0]
    if 'card_faces' in firstResult:
        for entry in firstResult['card_faces']:
            message = discord.Embed(
                title="**{}**".format(entry['name']),
                url=firstResult['scryfall_uri'],
                color=COLOUR
            )
            message.set_image(url=entry['image_uris']['normal'])
            messages.append(message)
        return messages
    
    message = discord.Embed(
        title="**{}**".format(firstResult['name']),
        url=firstResult['scryfall_uri'],
        color=COLOUR
    )

    message.set_image(url=firstResult['image_uris']['normal'])
    messages.append(message)
    return messages

client.run(os.environ.get("DISCORD"))
