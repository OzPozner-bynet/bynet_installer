FROM python:3.10-slim

WORKDIR /app

COPY ./src/requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80
