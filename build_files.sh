#!/bin/bash

echo "Running Build Script..."

# Install python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p static
mkdir -p staticfiles

# Create a placeholder file to ensure static directory isn't empty
echo "/* Placeholder file to ensure directory isn't empty */" > static/placeholder.css

# Run collectstatic with clear to ensure clean collection
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
