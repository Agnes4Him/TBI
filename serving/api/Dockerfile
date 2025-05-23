FROM python:3.12.4

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "model.py", "./" ]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "model:app", "-b", "0.0.0.0:4000", "-w", "4" ]