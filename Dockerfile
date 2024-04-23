# Use the official Python 3.11.6 image as base
FROM python:3.11.6

# Set PYTHONUNBUFFERED environment variable
ENV PYTHONUNBUFFERED True

# Set the working directory in the container
WORKDIR /app

# Copy only necessary files into the container
COPY . .

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

# Expose port 5000 to the outside world
EXPOSE 5000

# Set environment variables
ENV PORT=5000

# Command to run the Flask application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
