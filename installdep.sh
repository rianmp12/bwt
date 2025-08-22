#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Install libraries from requirements.txt
pip install -r requirements.txt

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Libraries were successfully installed."
else
    echo "An error occurred during the installation."
fi