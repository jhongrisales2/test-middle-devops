FROM alpine:3.20

RUN apk add --no-cache python3-dev
RUN apk add py3-pip \
    && pip3 install --upgrade pip --break-system-packages

WORKDIR /app-flask

COPY . /app-flask

RUN pip3 --no-cache-dir install -r requirements.txt --break-system-packages

CMD ["python3","first_app/app_random_names.py"]