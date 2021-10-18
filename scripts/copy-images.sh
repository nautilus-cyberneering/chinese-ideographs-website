#!/bin/bash

# Find and copy Base images from data folder to public folder

# TODO: use a domain app to extract the list of Base images. Remove magic numbers.

# Find Base images
echo "Find Base images ..."
find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)

# Copy all Base images to public folder
echo "Copying Base images to public folder ..."
find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec cp -fv {} ./public/images \;