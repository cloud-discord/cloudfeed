#!/usr/bin/python3
import os
import discord # type: ignore

from logging import config, getLogger
from asyncio import Queue

from cloudfeed.article import Article

config.fileConfig('confs/logging.conf')
logger = getLogger(__name__)


token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready() -> None:
    article_queue: Queue = Queue(maxsize=20)
    logger.info(f'Article queue initialized with size {article_queue.qsize()}')
    logger.info(f'{client.user} has connected to Discord!')


if __name__ == "__main__":
    logger.info(f'Starting up...')
    client.run(token)
