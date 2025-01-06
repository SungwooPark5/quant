# Pull base image
FROM python:3.12.6-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

RUN apt-get update
# RUN apt-get install -y gcc
# RUN apt-get install -y default-libmysqlclient-dev
# RUN apt-get update && apt-get install -y pkg-config

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .