FROM python:3.13

RUN pip install uv

RUN mkdir /app

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen
