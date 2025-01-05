FROM python:3.12-alpine
WORKDIR /app
RUN python -m venv .zipline
COPY requirements.txt requirements.txt
RUN source .zipline/bin/activate
RUN pip install -r requirements.txt
CMD ["python","app.py"]
