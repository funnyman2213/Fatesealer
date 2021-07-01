import asyncio
import discord
import os
import re
import aiohttp

client = discord.Client()
client.aiohttp_session = aiohttp.ClientSession(loop=client.loop)

async def getRequest(url, **kwargs):
    await asyncio.sleep(0.1)
    async with client.aiohttp_session.get(url, **kwargs) as response:
        return await response.json()

async def getFormattedCard(name: str) -> list[discord.Embed]:
    card = await getRequest(url='http://api.scryfall.com/cards/named?', params={'fuzzy':name})
    messages: list[discord.Embed] = list()

    if card['object'] == 'error':
        return discord.Embed(
            description = "an error has occured. {}".format(re.sub(r'\(|\'|,|\)+', '', card['details']))
        )
    
    if 'card_faces' in card:
        for entry in card['card_faces']:
            message = discord.Embed(
                title="**{}**".format(entry['name']),
                url=card['scryfall_uri'],
                color=discord.Colour(0x1b6f9)
            )
            message.set_image(url=entry['image_uris']['normal'])
            messages.append(message)
        return messages
    
    message = discord.Embed(
        title="**{}**".format(card['name']),
        url=card['scryfall_uri'],
        color=discord.Colour(0x1b6f9)
    )

    message.set_image(url=card['image_uris']['normal'])
    messages.append(message)
    return messages

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
            for name in groups:
                cards = await getFormattedCard(name)
                for card in cards:
                    await message.channel.send(embed=card)

client.run(os.environ.get("DISCORD"))