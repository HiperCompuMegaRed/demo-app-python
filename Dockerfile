# Use an official Python runtime as a parent images
FROM docker.io/library/python:latest

# Create a directory for your app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src /app

# Install any needed packages specified in requirements.txt
# If you don't have any requirements, you can remove this line
RUN pip install flask
# Expose port 8080 for the application
EXPOSE 8080

# Define a command to run your application
CMD ["python", "app.py"]

