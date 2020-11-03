FROM python:3.9-slim-buster

RUN pip install pipenv
COPY Pipfile /usr/src/app/Pipfile
WORKDIR /usr/src/app
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY ./src /usr/src/app

CMD ["python", "api.py"]