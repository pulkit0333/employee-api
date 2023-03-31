FROM python:3.10
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY Pipfile Pipfile.lock /app/
RUN python3 -m pip install pipenv &&  \
    pipenv install --system --deploy

COPY src .