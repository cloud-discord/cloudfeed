# CloudFeed Bot

Simple discord bot to post messages into a channel written in python

## Setup dev environment

First you need to install python. If you use a debian based distro you can use these commands:
```
wget https://raw.githubusercontent.com/joaonsantos/SmallScripts/master/install-python-pip-pipenv.sh
chmod +x install-python-pip-pipenv.sh
./install-python-pip-pipenv.sh 3.8
```

This installs python3.8, pip and pipenv.

## Install project dependencies

To install project dependencies:
```
pipenv install
```

## Running the project

To run the project use:
```
pipenv run main
```

Run in development mode:
```
pipenv run dev
```

Clean artifacts:
```
pipenv run clean
```

