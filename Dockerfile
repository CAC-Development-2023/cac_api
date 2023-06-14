# Author: Sable <sable262021[at]gmail[dot]com>
# Last Modified: 14/6/2023

FROM python:3.11

WORKDIR /code

COPY ./models /code/models

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./cac_api /code/cac_api
COPY ./cac_vue_fontend /code/cac_vue_fontend
COPY ./tests /code/tests

RUN black -l 79 /code/cac_api
RUN black -l 79 /code/tests
RUN isort --multi-line 3 --profile black /code/cac_api
RUN isort --multi-line 3 --profile black /code/tests
RUN flake8 --max-doc-length=72 --ignore=E203 /code/cac_api
RUN flake8 --max-doc-length=72 --ignore=E203 /code/tests


CMD ["uvicorn", "cac_api.main:app", "--host", "0.0.0.0", "--port", "80"]