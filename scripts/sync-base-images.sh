#!/bin/bash

# Find and copy Base images from data folder to public folder

# TODO: use a domain app to extract the list of Base images. Remove magic numbers.

# Show current Base images
echo "Current Base images in website ..."
find ./public/images -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)

# Find Base images
echo "Find Base images in library ..."
find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)

# Remove all Base images from public folder
echo "Removing Base images from public folder ..."
find ./public/images -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec rm -f {} \;

# Copy all Base images from library to public folder
echo "Copying Base images to public folder ..."
find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec cp -fv {} ./public/images \;