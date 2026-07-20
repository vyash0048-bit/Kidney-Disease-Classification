FROM python:3.10-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the Flask app runs on
EXPOSE 8080

CMD ["python", "app.py"]
