# Prepare the base environment.
FROM python:3.7.8-slim-buster as builder_base_waherb
MAINTAINER asi@dbca.wa.gov.au
RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y wget git libmagic-dev gcc binutils gdal-bin proj-bin python3-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip

# Install Python libs using poetry.
FROM builder_base_waherb as python_libs_waherb
WORKDIR /app
ENV POETRY_VERSION=1.0.5
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Install the project.
FROM python_libs_waherb
COPY manage.py gunicorn.py ./
COPY crossreference ./crossreference
COPY graphic ./graphic
COPY herbarium ./herbarium
COPY naturemap ./naturemap
COPY nomenclature ./nomenclature
COPY waherb ./waherb
RUN python manage.py collectstatic --noinput
# Run the application as the www-data user.
USER www-data
EXPOSE 8080
CMD ["gunicorn", "waherb.wsgi", "--config", "gunicorn.py"]
