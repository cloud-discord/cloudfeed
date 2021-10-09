import logging

import discord
from discord.ext import commands

from cloudfeed import music
from cloudfeed import config
from cloudfeed import botutils

logger = logging.getLogger(__name__)

client = commands.Bot(command_prefix=commands.when_mentioned_or('$'))


@client.event
async def on_ready() -> None:
    botutils.list_info(client)
    logger.info(f'Ready')


@client.command(name="play", help="Play a youtube music video")
async def play_music(ctx: commands.Context, url: str):
    await _ensure_voice(ctx)

    async with ctx.typing():
        player = await music.YTDLSource.from_url(url)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))


@client.command(name="stop", help="Stop youtube music video")
async def stop(ctx: commands.Context):
    await ctx.voice_client.disconnect()

async def _ensure_voice(ctx):
    if ctx.voice_client is None:
        if ctx.author.voice:
            try:
                await ctx.author.voice.channel.connect()
            except discord.errors.ClientException as e:
                logger.error(f"already connected to a voice channel: {e}")
        else:
            await ctx.send("You are not connected to a voice channel.")
            raise commands.CommandError("Author not connected to a voice channel.")
    elif ctx.voice_client.is_playing():
        ctx.voice_client.stop()

if __name__ == "__main__":
    logger.info(f'Starting up...')
    client.run(config.DISCORD_TOKEN)
