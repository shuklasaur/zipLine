FROM python:3.12-alpine AS prod
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python","app.py"]


FROM python:3.12-alpine AS dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apk add git \
&& apk add openssh \
&& pip install --no-cache-dir --upgrade -r requirements.txt 
CMD ["sh"]
