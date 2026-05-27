FROM ubuntu:22.04

LABEL maintainer="Decoded Security <erich.winkler@decodedsecurity.com>"
LABEL description="Decoded Security Hashing Lab - Password Cracking"
LABEL version="1.0"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    less \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /lab/wordlists /lab/scripts

COPY hashes.txt /lab/hashes.txt
COPY hashes_md5.txt /lab/hashes_md5.txt
COPY hashes_sha1.txt /lab/hashes_sha1.txt
COPY hashes_bcrypt.txt /lab/hashes_bcrypt.txt
COPY wordlists/decoded_wordlist.txt /lab/wordlists/decoded_wordlist.txt
COPY scripts/welcome.sh /lab/scripts/welcome.sh
COPY scripts/crack.py /lab/scripts/crack.py
COPY scripts/hints.txt /lab/hints.txt

RUN chmod +x /lab/scripts/welcome.sh /lab/scripts/crack.py

WORKDIR /lab

CMD ["/bin/bash", "-c", "/lab/scripts/welcome.sh && /bin/bash"]
