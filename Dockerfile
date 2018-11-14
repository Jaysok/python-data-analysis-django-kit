FROM tiangolo/uwsgi-nginx:python3.5

ENV UWSGI_INI /sampleapp/uwsgi.ini

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY nginx.docker.conf /etc/nginx/conf.d/nginx.conf
COPY uwsgi.ini /sampleapp/
COPY ./sampleapp /sampleapp

WORKDIR /sampleapp
