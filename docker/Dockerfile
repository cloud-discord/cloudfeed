FROM ubuntu:19.10 AS build

WORKDIR /opt/app

RUN apt-get -qq update && apt-get install -qq -y \
    python3.8 \
    python3.8-dev \
    python3.8-venv \
    python3.8-distutils \
    wget

# Get pip
RUN wget -q -O get-pip.py "https://bootstrap.pypa.io/get-pip.py"

# Copy dependency declarations to container folder
COPY ./pyproject.toml ./poetry.lock /opt/app/

# Add pip to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Setup pip
RUN python3.8 get-pip.py -q \
  && python3.8 -m pip install -q --user poetry

ENV PATH="/opt/app/.venv/bin:$PATH" VIRTUAL_ENV="/opt/app/.venv"

RUN python3.8 -m venv .venv \
  && poetry config virtualenvs.in-project true \
  && poetry install --no-dev


FROM ubuntu:19.10

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
WORKDIR /opt/app

RUN apt-get -qq update && apt-get install -qq -y \
    python3.8 \
    ca-certificates \
  && apt-get -qq autoremove \
  && rm -rf /var/lib/apt/lists/*

# Copy built venv
COPY --from=build /opt/app/.venv /opt/venv/

# Make sure venv is used
ENV PATH="/opt/venv/bin:${PATH}" VIRTUAL_ENV="/opt/venv"

# Copy files from current dir to container folder
COPY . /opt/app/

CMD ["bash", "-c", "python bot.py"]
