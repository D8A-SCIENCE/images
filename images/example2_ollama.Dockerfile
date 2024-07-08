# Use an official Python runtime as a parent image
FROM ollama/ollama:latest

# Set the working directory in the container
WORKDIR /app

# Install Prefect 2
RUN pip install --ignore-installed prefect-kubernetes

# Copy the current directory contents into the container at /app
ADD . /app

# Run when the container launches
CMD ["prefect", "version"]

