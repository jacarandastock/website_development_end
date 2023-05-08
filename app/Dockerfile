# Use the official Python image as the base image
FROM python:3.9-alpine

# Install any required system packages (if needed)
RUN apk add --no-cache build-base

# Copy the requirements.txt file into the container
COPY ./requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade --user -r requirements.txt

# Copy the application source code into the container
COPY src /app

WORKDIR /src

# Start the application
CMD ["python3", "main.py"]
