# Use the official VS Code Python image as the base image.
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Avoid warnings by switching to noninteractive mode.
ENV DEBIAN_FRONTEND=noninteractive

# Install any system dependencies your app might need.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    nodejs \
    npm \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
WORKDIR /workspace

# (Optional) Copy the rest of your project if not using a bind mount.
# COPY . .

# Verify npm installation
RUN node -v && npm -v