#!/usr/bin/env bash
# build.sh - Render build script

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements-deploy.txt

echo "Creating necessary directories..."
mkdir -p uploads
mkdir -p models

echo "Build completed successfully!"
