FROM python:3.9-alpine

RUN pip install pipenv
COPY ./src /usr/src/app
COPY Pipfile /usr/src/app
WORKDIR /usr/src/app
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app.py"]