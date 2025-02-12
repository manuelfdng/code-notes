#!/bin/bash

# Step 1: Build the Docker image
echo "Building the Docker image..."
docker build --platform linux/amd64 <folder-name>

# Step 2: Get the IMAGE ID of the latest image
echo "Fetching the IMAGE ID of the latest image..."
image_id=$(docker images --filter "dangling=true" --format "{{.ID}}" | head -n 1)

if [ -z "$image_id" ]; then
    echo "Error: Could not fetch the IMAGE ID. Ensure the image was built successfully."
    exit 1
fi

echo "Latest IMAGE ID fetched: $image_id"

# Step 3: Tag the image
new_tag=<gcr-tag>
echo "Tagging the image as $new_tag..."
docker tag "$image_id" "$new_tag"

# Step 4: Push the image to the GCR repository
echo "Pushing the image to the GCR repository..."
docker push "$new_tag"

if [ $? -eq 0 ]; then
    echo "Image successfully pushed to $new_tag."
else
    echo "Error: Failed to push the image."
    exit 1
fi