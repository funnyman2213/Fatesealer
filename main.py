import os
import re

import discord

from cards import *

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

client.run(os.environ.get("DISCORD"))
