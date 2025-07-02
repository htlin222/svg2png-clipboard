#!/bin/bash
# Simple script to publish to PyPI

set -e

echo "🚀 Publishing svg2png-clipboard to PyPI"
echo "======================================="

# Check if version was updated
echo "Current version in pyproject.toml:"
grep "version = " pyproject.toml

read -p "Have you updated the version? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please update the version in pyproject.toml first!"
    exit 1
fi

# Clean up
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Build
echo "📦 Building package..."
python -m build

# Check
echo "✅ Checking package..."
twine check dist/*

# Show what will be uploaded
echo "📋 Files to be uploaded:"
ls -la dist/

# Confirm upload
read -p "Upload to PyPI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📤 Uploading to PyPI..."
    twine upload dist/*
    echo "✅ Done! Package uploaded successfully."
    echo "🎉 Install with: pip install svg2png-clipboard"
else
    echo "❌ Upload cancelled."
fi