# Dockerfile for Adjective-Noun Generator API
# Base image from Python slim
FROM python:slim

# Set working directory
WORKDIR /usr/src/app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=random_word_api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask application
CMD ["gunicorn", "wsgi:app"]
