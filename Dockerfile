#docker build -t verify-json-app .

#docker run verify-json-app

FROM python:3.9-slim

WORKDIR /app

COPY . /app

CMD ["python", "-m", "unittest", "test.py"]