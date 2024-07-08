# Use an official Python runtime as a parent image
FROM ollama/ollama:latest

# Set the working directory in the container
WORKDIR /app

# Install common packages
#This is not strictly required
RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    git-lfs \
    python3.10 \
    python3-pip

# Install Prefect 2
RUN pip install --ignore-installed prefect-kubernetes==0.3.10

# Copy the current directory contents into the container at /app
ADD . /app

# Run when the container launches
CMD ["prefect", "version"]

