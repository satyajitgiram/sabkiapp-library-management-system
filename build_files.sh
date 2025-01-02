#!/bin/bash

echo "Running Build Script..."


pip install -r requirements.txt
python3 manage.py collectstatic --no-input --clear


echo "Build Script Completed!"
