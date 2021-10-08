import logging

from cloudfeed import config

logger = logging.getLogger(__name__)


def list_info(client):
    logger.info(f'{client.user} has connected to Discord!')
    guilds = client.guilds

    for guild in guilds:
        guild_name = guild.name
        logger.info(f'Found guild -> {guild_name}')

        if guild_name == config.GUILD_NAME:
            channels = guild.channels

            for channel in channels:
                channel_name = channel.name
                logger.info(f'Found channel -> {channel_name}')
