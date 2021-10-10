# CloudFeed Bot

Discord bot that provides music and news feed features.

## Setup dev environment

To set up the development environment python and poetry must be installed.

### Python

This project requires Python 3.10. Please visit https://www.python.org/downloads/release/python-3100 to install it.

### Poetry

This project requires poetry 1.2.0a2. To install please visit https://python-poetry.org/docs/master/#installation.
<br/>
Make sure to set `$POETRY_VERSION=1.2.0a2`. Check with `poetry --version` after installing.

Make sure to add poetry binary executable path to `$PATH`, by default `$HOME/.local/bin`.

### Virtual Environment

To create the project virtual environment where your dependencies will live, run the following:
```bash
$ poetry env use 3.10 # ensure poetry uses python 3.10
```

```bash
$ poetry shell # sets the current shell environment to use the virtualenv settings
```

```bash
$ poetry install # install all dependencies, including dev dependencies
```

### FFmpeg

Since this bot has media capabilities, it requires a media library to be available in the system.

One such library is FFmpeg, to learn more and install please visit https://www.ffmpeg.org.

## Running the project

This project requires a discord app token to connect do discord. Please set `$DISCORD_TOKEN`.
<br/>
For more information, please visit https://discord.com/developers/docs/intro.

Inside the virtualenv run:
```bash
python bot.py
```

Running in docker:
```bash
docker build -t cloudfeedbot -f docker/Dockerfile .
docker run -e DISCORD_TOKEN=$DISCORD_TOKEN cloudfeedbot
```

### Interacting with the Bot

When the bot is up and running to interact with it simply mention it using `@` or use the command prefix `$`.
