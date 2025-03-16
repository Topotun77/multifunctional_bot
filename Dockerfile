FROM python:3.12

RUN mkdir /multifunctional_bot

WORKDIR /multifunctional_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python main.py
