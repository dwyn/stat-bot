# Use the official Python image from the DockerHub
FROM python:3.9-slim

# Set the maintainer label
LABEL maintainer="10413171+dwyn@users.noreply.github.com"

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./stat-bot.py" ]
