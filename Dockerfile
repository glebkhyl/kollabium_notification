FROM python:3.13

# Установка uv
RUN pip install uv

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

# Использование uv вместо pip
RUN uv pip install -r requirements.txt