FROM python:3.11-slim

WORKDIR /app

COPY ./basic_example/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./basic_example/client.py .

ENTRYPOINT ["python", "client.py"]
