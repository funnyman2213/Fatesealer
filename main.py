import os
import re
import asyncio
import re

import fateseal
import fateseal.request

import aiohttp
import discord

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
    card: fateseal.Card = await fateseal.request.cards.Named(fuzzy=name).async_get()
    messages: list[discord.Embed] = list()

    if card.object == 'error':
        error: fateseal.Error = card
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', error.details))
        ),]
    
    if card.card_faces:
        for entry in card.card_faces:
            message = discord.Embed(
                title="**{}**".format(entry.name),
                url=card.scryfall_uri,
                color=COLOUR
            )
            message.set_image(url=entry.image_uris.normal)
            messages.append(message)
        return messages
    
    message = discord.Embed(
        title="**{}**".format(card.name),
        url=card.scryfall_uri,
        color=COLOUR
    )

    message.set_image(url=card.image_uris.normal)
    messages.append(message)
    return messages

async def getCardFromSearch(search: str) -> list[discord.Embed]:
    objlist = await fateseal.request.cards.Search(search).async_get()
    messages: list[discord.Embed]= list()
    
    # returns if error ie. no results found
    if objlist.object == 'error':
        objlist: fateseal.Error = objlist
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', objlist.details))
        ),]

    objlist: fateseal.ObjList = objlist
    # returns the first result of the search
    card: fateseal.Card = objlist.data[0]
    if card.card_faces:
        for entry in card.card_faces:
            message = discord.Embed(
                title="**{}**".format(entry.name),
                url=card.scryfall_uri,
                color=COLOUR
            )
            message.set_image(url=entry.image_uris.normal)
            messages.append(message)
        return messages
    
    message = discord.Embed(
        title="**{}**".format(card.name),
        url=card.scryfall_uri,
        color=COLOUR
    )

    message.set_image(url=card.image_uris.normal)
    messages.append(message)
    return messages

client.run(os.environ.get("DISCORD"))
