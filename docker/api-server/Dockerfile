FROM alpine:3.10.1@sha256:6a92cd1fcdc8d8cdec60f33dda4db2cb1fcdcacf3410a8e05b3741f44a9b5998

LABEL corporation="Aquila Systems Corp."
LABEL maintainer="G22U"
LABEL email="contact@aquila.company"

WORKDIR /raven

COPY . .

# necessary packages
RUN set -ex; \
    apk add --update --no-cache \
    postgresql-client \
    jpeg-dev \
    python3

# these temp installations will be removed at the end
RUN set -ex; \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc \
    g++ \
    libc-dev \
#    libpq-dev \
    postgresql-dev \
    linux-headers \
    musl-dev \
    zlib \
    zlib-dev \
    python3-dev

# installation
RUN set -ex; \
    pip3 install --upgrade pip; \
    pip3 install -r requirements.txt

# remove temp installations
RUN apk del .tmp-build-deps

# create user
RUN adduser -D raven
USER raven
