FROM python:3-slim-buster AS base

# Export ARGs as ENV vars so they can be shared among steps
ENV DEBIAN_FRONTEND=noninteractive \
    APT_OPTS="-q=2 --yes"

FROM base AS builder-deps
# Install build dependencies
RUN apt ${APT_OPTS} update && \
    apt ${APT_OPTS} --no-install-recommends install apt-utils && \
    apt ${APT_OPTS} --no-install-recommends install \
      python3 \
      python3-pip

FROM builder-deps AS builder
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["bash","start.sh"]
