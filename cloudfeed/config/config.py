import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


CHANNEL_NAME = os.getenv('CHANNEL_NAME')
OUTPUT_CHANNEL = os.getenv('OUTPUT_CHANNEL')
GUILD_NAME = os.getenv('GUILD_NAME')
REPLY_TIMEOUT = os.getenv('REPLY_TIMEOUT', 60)
ARTICLE_INTERVAL = os.getenv('ARTICLE_INTERVAL', 86400)
QUEUE_MAXSIZE = os.getenv('QUEUE_MAXSIZE', 20)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
