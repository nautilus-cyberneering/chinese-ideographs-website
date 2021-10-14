#!/bin/bash

# Find and copy Base images from data folder to public folder

# Find Base images
echo "Find Base images ..."
find ./data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)

# Copy all Base images to public folder
echo "Copying Base images to public folder ..."
find ./data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec cp {} ./public/images \;