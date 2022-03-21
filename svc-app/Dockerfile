FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

WORKDIR /svc-app

RUN apt-get update \
  && apt-get -y install apt-utils curl netcat iputils-ping \
  && apt-get clean

COPY ./requirements.txt ./requirements-dev.txt /svc-app/

RUN pip install --upgrade pip --no-cache-dir -r /svc-app/requirements-dev.txt

COPY ./app /svc-app/app

EXPOSE $PORT

ENTRYPOINT ["./entrypoint.sh"]