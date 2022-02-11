FROM python:3.9
MAINTAINER Ryan Goodwin

RUN pip install pipenv

WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy
COPY app /code/backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
