FROM python:3-alpine

WORKDIR /exem_4week

COPY ./app/requirements.txt requirements.txt

RUN apk update && apk add python3-dev
RUN  pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "app/main.app"]