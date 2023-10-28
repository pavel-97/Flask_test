FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBBUFFERED 1
EXPOSE 8080

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .