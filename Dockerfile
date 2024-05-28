# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# COPY config.yaml config.yaml
# COPY .env .env
COPY tools/ tools/
COPY utils/ utils/
COPY telegram.py telegram.py 

#for normal deploy
ENTRYPOINT ["/app/python", "telegram.py"]

