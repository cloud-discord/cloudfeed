import os

from discord.ext import commands as discord
from logging import config, getLogger
from asyncio import Queue, TimeoutError

from cloudfeed.article import Article

config.fileConfig('confs/logging.conf')
logger = getLogger(__name__)

CHANNEL_NAME = os.getenv('CHANNEL_NAME')
GUILD_NAME = os.getenv('GUILD_NAME')
REPLY_TIMEOUT = os.getenv('REPLY_TIMEOUT', 30.0)
token = os.getenv('DISCORD_TOKEN')

client = discord.Bot(command_prefix='$')
article_queue: Queue = Queue(maxsize=20)

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
  logger.info(f'Article queue initialized with size {article_queue.qsize()}')
  logger.info(f'{client.user} has connected to Discord!')

  list_info()
  logger.info(f'Ready')


@client.command(name='new', help='Adds a new article to the queue.')
async def new_article(ctx):
  channel = ctx.channel

  if channel.name == CHANNEL_NAME:
    await channel.send('What is the title of the article?')

    def title_check(reply):
      if reply.author == ctx.message.author:
        return str(reply.content)

    try:
      title = await client.wait_for('message', timeout=REPLY_TIMEOUT, check=title_check)
    except TimeoutError:
      await channel.send('You took too long to respond! Are you sleeping? 💤')
    else:
      await channel.send(f'Got -> {title.content}')

  if channel.name == CHANNEL_NAME:
    await channel.send('What is the url of the article?')

    def url_check(reply):
      if reply.author == ctx.message.author:
        return str(reply.content)

    try:
      url = await client.wait_for('message', timeout=REPLY_TIMEOUT, check=url_check)
    except TimeoutError:
      await channel.send('You took too long to respond! Are you sleeping? 💤')
    else:
      await channel.send(f'Got -> {url.content}')


  if channel.name == CHANNEL_NAME:
    await channel.send('Do you have any comments on the article?')

    def comments_check(reply):
      if reply.author == ctx.message.author:
        return str(reply.content)

    try:
      comments = await client.wait_for('message', timeout=60.0, check=comments_check)
    except TimeoutError:
      await channel.send('You took too long to respond! Are you sleeping? 💤')
    else:
      await channel.send(f'Got -> {comments.content}')

  await channel.send(f'Storing article in queue...')
  await article_queue.put(Article(title=title, link=url, description=comments))
  await channel.send(f'Done!')


if __name__ == "__main__":
  logger.info(f'Starting up...')
  client.run(token)
