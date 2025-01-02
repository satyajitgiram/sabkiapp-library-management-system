#!/bin/bash

echo "Running Build Script..."


pip install -r requirements.txt
python3 manage.py collectstatic --noinput


echo "Build Script Completed!"
