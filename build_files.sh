#!/bin/bash

echo "Running Build Script..."

# Install python dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p staticfiles/static

# Run collectstatic
python manage.py collectstatic --noinput

echo "Build completed successfully!"
