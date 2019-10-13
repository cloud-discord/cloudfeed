FROM ubuntu:19.04

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# Install deps, clean apt cache
RUN apt-get -qq update && apt-get install -qq -y \
    python3.8 \
    python3.8-dev \
    python3.8-distutils \
    wget \
  && apt-get -qq autoremove \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN useradd -ms /bin/bash ubuntu \
  && chown -R ubuntu .

USER ubuntu

# Get pip
RUN wget -q -O get-pip.py "https://bootstrap.pypa.io/get-pip.py"

# Add pip-related stuff to PATH
ENV PATH="${PATH}:/home/ubuntu/.local/bin"

# Copy Pipfiles from current dir to container folder
COPY --chown=ubuntu ./Pipfile* ./

# Setup pipvenv and deps
RUN python3.8 get-pip.py -q --user \
  && pip3.8 install -q --user pipenv \
  && pipenv --bare --python 3.8 \
  && pipenv sync \
  && rm get-pip.py

# Copy files from current dir to container folder
COPY --chown=ubuntu . /app

CMD ["bash", "-c", "pipenv run main"]
