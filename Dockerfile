# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m appuser

# Set the working directory
WORKDIR /weather-api

# Create application directory and set permissions
RUN mkdir -p /weather-api && chmod -R 777 /weather-api

# Copy only requirements first for caching
COPY requirements.txt /weather-api/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /weather-api/

# Change to non-root user
USER appuser

# Expose the application port
EXPOSE 80

# Run the application
CMD ["python", "main.py"]
