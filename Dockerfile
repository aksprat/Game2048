# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
