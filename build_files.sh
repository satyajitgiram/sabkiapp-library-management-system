#!/bin/bash

echo "Running Build Script..."

# Install python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p static
mkdir -p staticfiles/static

# Create a placeholder file to ensure static directory isn't empty
echo "/* Placeholder file to ensure directory isn't empty */" > static/placeholder.css

# Run collectstatic
python manage.py collectstatic --noinput

echo "Build completed successfully!"
