FROM python:3.10 AS build

WORKDIR /opt/app

# Copy dependency declarations to container folder
COPY ./pyproject.toml ./poetry.lock /opt/app/

RUN pip install virtualenv

# Setup poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_PREVIEW=1 python -

ENV PATH="/root/.local/bin:/opt/app/.venv/bin:$PATH" VIRTUAL_ENV="/opt/app/.venv"

RUN poetry --version

RUN python3.10 -m venv .venv \
  && poetry config virtualenvs.in-project true \
  && poetry install --no-root --no-dev

FROM python:3.10

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
WORKDIR /opt/app

# Copy built venv
COPY --from=build /opt/app/.venv /opt/venv/

# Make sure venv is used
ENV PATH="/opt/venv/bin:${PATH}" VIRTUAL_ENV="/opt/venv"

RUN apt-get update && apt-get -y install ffmpeg

# Copy files from current dir to container folder
COPY . /opt/app/

CMD ["python", "bot.py"]
