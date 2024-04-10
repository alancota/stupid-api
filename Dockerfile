FROM python:3.12.2

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/stupid_api /app/stupid_api