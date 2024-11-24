# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

LABEL author="Shuailin Pan (LeConjuror)"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gcc \
    python3 \
    pip \
    socat

RUN pip install pwn --break-system-packages

COPY flag.txt /home/valley/flag.txt
COPY valley.c /home/valley/valley.c
COPY solution.py /home/valley/solution.py

RUN gcc -g -o /home/valley/valley /home/valley/valley.c

RUN chmod 400 /home/valley/flag.txt
RUN chmod 755 /home/valley/valley
RUN chmod 755 /home/valley/valley.c
RUN chmod 777 /home/valley/solution.py

WORKDIR /home/valley

RUN mkdir /challenge && chmod 700 /challenge

# Create artifacts for players to download
RUN tar zcvf /challenge/artifacts.tar.gz valley.c

# make sure you put the flag here so cmgr and pico can check submissions
RUN echo "{\"flag\":\"$(cat /home/valley/flag.txt)\"}" > /challenge/metadata.json


EXPOSE 5555
# PUBLISH 5555 AS port

CMD ["socat", "tcp-listen:5555,reuseaddr,fork", "SYSTEM:'./valley'"]
#CMD ["tail", "-f", "/dev/null"]
