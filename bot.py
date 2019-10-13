#!/usr/bin/python3
import os
from logging import config, getLogger

import discord

config.fileConfig('confs/logging.conf')
logger = getLogger(__name__)

token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready() -> None:
  logger.info(f'{client.user} has connected to Discord!')


if __name__== "__main__":
  logger.info(f'Starting up...')
  client.run(token)
