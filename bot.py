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
QUEUE_MAXSIZE = os.getenv('QUEUE_MAXSIZE', 20)
token = os.getenv('DISCORD_TOKEN')

client = discord.Bot(command_prefix='$')
article_queue: Queue = Queue(maxsize=QUEUE_MAXSIZE)

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

async def question_user(attribute, channel):
  question = ''

  if attribute == 'title':
    question = 'What is the title of the article?'
  elif attribute == 'url':
    question = 'What is the url of the article?'
  elif attribute == 'comments':
    question = 'Do you have any comments on the article?'

  await channel.send(question)

async def get_user_response(command_author, channel):
  def reply_check(reply):
    if reply.author == command_author:
      return str(reply.content)

  try:
    return await client.wait_for('message', timeout=REPLY_TIMEOUT, check=reply_check)
  except TimeoutError:
    await channel.send('You took too long to respond! Are you sleeping? 💤')
    logger.error('No response was provided by user...')
    raise ValueError('No response was provided by user')

@client.command(name='new', help='Adds a new article to the queue.')
async def new_article(ctx):
  channel = ctx.channel
  author = ctx.message.author

  if channel.name == CHANNEL_NAME:
    try:
      await question_user('title', channel)
      title = await get_user_response(author, channel)

      await question_user('url', channel)
      url = await get_user_response(author, channel)

      await question_user('comments', channel)
      comments = await get_user_response(author, channel)

      await channel.send(f'Storing article in queue...')
      await article_queue.put(Article(title=title, link=url, description=comments))
      logger.debug(f'Stored article with title {title.content}, link {url.content} and description {comments.content}')

      logger.info(f'New article stored in queue')
      logger.info(f'Queue size is now {article_queue.qsize()}')
      await channel.send(f'Done! 🌟')
    except ValueError:
        logger.error('Unable to create article')


if __name__ == "__main__":
  logger.info(f'Starting up...')
  client.run(token)

