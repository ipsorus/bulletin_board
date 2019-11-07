FROM python:3.7.3-alpine
RUN apk add --no-cache curl make gcc libc-dev linux-headers musl-dev tk-dev tcl-dev openssl-dev libffi-dev mysql-client mariadb-dev python3-dev jpeg-dev zlib-dev freetype-dev lcms2-dev tiff-dev openjpeg-dev
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN  python /app/manage.py collectstatic --no-input && python /app/manage.py makemigrations && python /app/manage.py migrate
EXPOSE 80
ENTRYPOINT ["python", "/app/manage.py", "runserver", "0.0.0.0:80"]