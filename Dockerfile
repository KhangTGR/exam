FROM python:3-alpine

WORKDIR /exem_4week

COPY ./app/requirements.txt requirements.txt

RUN apk update && apk add python3-dev
RUN  pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD export FLASK_APP=main.py
CMD cd app/
CMD python3 /exem_4week/app/main.py
