FROM python:3-alpine

ADD ./requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

ADD ./app /app

EXPOSE 5000

WORKDIR /app

CMD [ "python3", "run.py" ]