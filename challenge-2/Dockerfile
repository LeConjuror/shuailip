# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

LABEL author="Shuailin Pan (LeConjuror)"

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && chmod 700 /challenge

COPY flag.txt /challenge/flag.txt
COPY red.png /app/
WORKDIR /app

# Create artifacts for players to download
RUN tar zcvf /challenge/artifacts.tar.gz red.png

# make sure you put the flag here so cmgr and pico can check submissions
RUN echo "{\"flag\":\"$(cat /challenge/flag.txt)\"}" > /challenge/metadata.json

CMD ["tail", "-f", "/dev/null"]
