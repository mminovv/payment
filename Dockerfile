ARG PYTHON_VERSION

FROM python:$PYTHON_VERSION as base

ENV ROOT /app
ENV PYTHONPATH "${PYTHONPATH}:/app/src/"

WORKDIR $ROOT

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock $ROOT/
RUN poetry install --no-root --no-dev

ADD alembic.ini .env $ROOT/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]