FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update && apt -y install libusb-1.0-0-dev
RUN pip3 install -r requirements.txt

COPY . .

CMD exec gunicorn --bind :8080 --workers 1 --timeout 0 main:app