# Use Python 3.9 slim version as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Command to run the Python application
CMD ["python", "app.py"]
