FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app
ENV HUGGINGFACEHUB_API_TOKEN=${HUGGINGFACEHUB_API_TOKEN}


CMD ["uvicorn", "lexi.sg-rag-backend-test.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
