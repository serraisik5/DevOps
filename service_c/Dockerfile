# parent image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /usr/src/app

COPY requirements.txt ./
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /usr/src/app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django to run in unbuffered mode
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Run the web server on port 8000
#Provides default command and parameters that will be executed when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "app_c.wsgi:application"]
