# Rebuild trigger 2025-10-20
FROM python:3.11-slim
...

# Use the official Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (so Docker caches installs)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Render expects
EXPOSE 8080

# Start the app using Gunicorn
CMD ["gunicorn", "nest_service:app", "--bind", "0.0.0.0:8080"]

