FROM ubuntu:trusty

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
    apt-get -y install \
              python \
              python-pip \
              make \
              build-essential \
              libssl-dev \
              zlib1g-dev \
              libbz2-dev \
              libreadline-dev \
              libsqlite3-dev \
              wget \
              curl \
              llvm \
              libncurses5-dev \
              zip \
              git-core \
              supervisor \
              sqlite

RUN mkdir -p /tmp
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /opt/program
ADD . /opt/program/apt-finder
