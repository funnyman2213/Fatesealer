import os
import re
from typing import List

import fateseal as fs
from fateseal.models import Error

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

async def getCardByName(name: str) -> list[discord.Embed]:
    card = await fs.Request[fs.cards.Named.return_type](fs.cards.Named(fuzzy=name)).async_get()
    messages: List[discord.Embed] = list()

    if not isinstance(card, Error):
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
    else:
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', card.details))
        ),]
    
    
async def getCardFromSearch(search: str) -> list[discord.Embed]:
    cards = await fs.Request[fs.cards.Search.return_type](fs.cards.Search(query=search)).async_get()
    messages: List[discord.Embed]= list()

    if not isinstance(cards, Error):
        card = cards[0]
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
    else:
        return [discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', cards.details))
        ),]

client.run(os.environ.get("DISCORD"))

