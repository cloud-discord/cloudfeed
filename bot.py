import os
import logging

import discord
from discord.ext import commands
import youtube_dl

from cloudfeed import config
from cloudfeed import botutils

logger = logging.getLogger(__name__)

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready() -> None:
    botutils.list_info(client)
    logger.info(f'Ready')


@client.command(name="play", help="Play a youtube music video")
async def play_music(ctx: commands.Context, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voice_channel: discord.VoiceChannel = discord.utils.get(
        ctx.guild.voice_channels, name="💬 Chilling")

    try:
        await voice_channel.connect()
    except discord.errors.ClientException as e:
        logger.error(f"already connected to a voice channel: {e}")

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command(name="stop", help="Stop youtube music video")
async def stop(ctx: commands.Context):
    voice: discord.VoiceClient = discord.utils.get(
        client.voice_clients, guild=ctx.guild)
    await voice.disconnect()


if __name__ == "__main__":
    logger.info(f'Starting up...')
    client.run(config.DISCORD_TOKEN)
