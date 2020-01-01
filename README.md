# CloudFeed Bot

Simple discord bot to post messages into a channel written in python

## Setup dev environment

First you need to install python. If you use a debian based distro you can use these commands:
```bash
wget https://raw.githubusercontent.com/joaonsantos/SmallScripts/master/install-python-pip-poetry.sh
chmod +x install-python-pip-poetry.sh
./install-python-pip-poetry.sh 3.8
```

This installs python3.8, pip and poetry.

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
