FROM python:3.12

COPY ./siteman /srv/www/siteman
WORKDIR /srv/www/siteman

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
