# Use Python 3.12 slim for a small footprint
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install system dependencies for audio/LiveKit
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uvicorn

# Copy project files
COPY . .

# Expose API port
EXPOSE 8000

# Start script
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]