FROM python:3.10-slim-buster

WORKDIR /app

# Install system dependencies if required by any ML libraries (e.g., opencv)
RUN apt-get update && apt-get install -y --no-install-recommends \
    awscli \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the Flask app runs on
EXPOSE 8080

CMD ["python", "app.py"]
