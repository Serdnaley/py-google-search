FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY static /app/static
COPY *.py .

EXPOSE 4000

CMD ["python", "server.py"]