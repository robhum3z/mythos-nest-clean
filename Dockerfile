# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to Render
EXPOSE 8080

# Run the app with Gunicorn (FastAPI via nest_service.py)
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "nest_service:app", "--bind", "0.0.0.0:8080"]

