# Этап, на котором выполняются подготовительные действия
FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Финальный этап
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

COPY ./src ./src

RUN apt-get update && \
    apt-get install libmagic1 -y

RUN pip install --no-cache /wheels/*
RUN pip install python-magic
RUN pip install google-cloud-storage

ENTRYPOINT ["python3", "src/main.py"]
