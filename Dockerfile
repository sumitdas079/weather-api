# Use a minimal Python image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies using apk
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    gcc \
    musl-dev \
    python3-dev \
    libressl-dev

# Create a non-root user and set workdir
RUN adduser -D appuser
WORKDIR /weather-api 

# Set permissions on the directory (as root)
RUN mkdir -p /weather-api && chmod -R 777 /weather-api

# Copy only requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optionally remove build dependencies to slim the image
RUN apk del build-base gcc musl-dev python3-dev libressl-dev libffi-dev

# Copy the rest of the application code
COPY . .

# Change to non-root user
USER appuser

# Expose the application port
EXPOSE 80

# Run the application
CMD ["python", "main.py"]
