FROM python:3.7.3-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache curl make gcc libc-dev linux-headers musl-dev tk-dev tcl-dev openssl-dev libffi-dev mysql-client mariadb-dev python3-dev jpeg-dev zlib-dev freetype-dev lcms2-dev tiff-dev openjpeg-dev

RUN mkdir /app
WORKDIR /app

COPY ./bulletin /app/bulletin
COPY ./bulletin_board /app/bulletin_board
RUN mkdir /app/media
COPY ./templates /app/templates
COPY ./user /app/user
COPY ./db_create.py /app/db_create.py
COPY ./get_html.py /app/get_html.py
COPY ./get_links.py /app/get_links.py
COPY ./manage.py /app/manage.py
COPY ./parser_auto.py /app/parser_auto.py
COPY ./parser_lib.py /app/parser_lib.py
COPY ./requirements.txt /app
COPY ./db.sqlite3 /app

RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]