
FROM ubuntu:bionic

RUN apt-get -qq update && apt-get install -q -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get -qq update && apt-get install -qy g++ gcc git wget curl unzip

COPY "awscliv2.zip" .
COPY "aws-sam-cli-linux-x86_64.zip" .

RUN unzip awscliv2.zip
RUN unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
RUN ./aws/install
RUN ./sam-installation/install

RUN sam --version

ENV __AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX
ENV __AWS_SECRET_ACCESS_KEY=yyyyyyyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

ENTRYPOINT /bin/bash
