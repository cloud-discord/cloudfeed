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

async def question_user(attribute):
  question = ''

  if attribute == 'title':
    question = 'What is the title of the article?'
  elif attribute == 'url':
    question = 'What is the url of the article?'
  elif attribute == 'comments':
    question = 'Do you have any comments on the article?'

  await channel.send(question)

async def get_user_response():
  def reply_check(reply):
    if reply.author == ctx.message.author:
      return str(reply.content)

  try:
    return await client.wait_for('message', timeout=REPLY_TIMEOUT, check=reply_check)
  except TimeoutError:
    await channel.send('You took too long to respond! Are you sleeping? 💤')
    raise Exception('No response was provided by user.')

@client.command(name='new', help='Adds a new article to the queue.')
async def new_article(ctx):
  channel = ctx.channel

  if channel.name == CHANNEL_NAME:
    await question_user('title')
    title = await get_user_response()

    await question_user('url')
    url = await get_user_response()

    await question_user('comments')
    comments = await get_user_response()

    await channel.send(f'Storing article in queue...')
    await article_queue.put(Article(title=title, link=url, description=comments))
    await channel.send(f'Done!')


if __name__ == "__main__":
  logger.info(f'Starting up...')
  client.run(token)

