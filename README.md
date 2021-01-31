# CloudFeed Bot

Discord bot to post articles into a Discord channel.

## Requirements

This project uses poetry to manage dependencies and create virtual environments.<br/>
To install poetry, visit https://python-poetry.org/docs/#installation.

Enable bash completion with https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh.

## Install project dependencies

To install project dependencies:
```bash
poetry install
```

## Running the project

To run the project use:
```bash
poetry run python bot.py
```

Run static type checks:
```bash
poetry run mypy --config-file .mypy.ini bot.py
```

If you prefer docker:
```bash
docker build -t cloudfeedbot -f docker/Dockerfile .
docker run cloudfeedbot
```

It is recommended to add pre commit hooks to contribute:
```
poetry install
poetry run pre-commit install
```
