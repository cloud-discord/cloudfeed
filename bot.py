#!/usr/bin/python3
import os

import discord

token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

client.run(token)
