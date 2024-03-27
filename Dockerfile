FROM python:3.10-bookworm

ENV PATH /usr/local/bin:$PATH

WORKDIR /spotflame

COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .  

RUN python manage.py makemigrations