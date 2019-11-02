#!/usr/bin/python3
import os
import discord # type: ignore

from logging import config, getLogger
from asyncio import Queue

from cloudfeed.article import Article

config.fileConfig('confs/logging.conf')
logger = getLogger(__name__)

CHANNEL_NAME = os.getenv('CHANNEL_NAME')
GUILD_NAME = os.getenv('GUILD_NAME')
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def list_info():
  guilds = client.guilds

  for guild in guilds:
    guild_name = guild.name
    logger.info(f'Found guild -> {guild_name}')

    if guild_name == GUILD_NAME:
      channels = guild.channels

      for channel in channels:
        channel_name = channel.name
        logger.info(f'Found channel -> {channel_name}')

@client.event
async def on_ready() -> None:
    article_queue: Queue = Queue(maxsize=20)
    logger.info(f'Article queue initialized with size {article_queue.qsize()}')
    logger.info(f'{client.user} has connected to Discord!')

  list_info()
  logger.info(f'Ready')

@client.event
async def on_message(message):
  if message.channel.name == CHANNEL_NAME:
    logger.info(f'Received message -> {message.content}')

    if message.content.startswith('$hey'):
      response = 'Hey there!'

      logger.info(f'Sent message -> {message.content}')
      await message.channel.send(response)

if __name__ == "__main__":
    logger.info(f'Starting up...')
    client.run(token)
