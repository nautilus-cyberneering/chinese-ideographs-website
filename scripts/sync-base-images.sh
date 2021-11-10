#!/bin/bash

# Find and copy Base images from data folder to public folder

# TODO: use a domain app to extract the list of Base images. Remove magic numbers.

if [[ ($1 == "") || ($1 == "show_website")]]
then
    # Show current Base images
    echo "Current Base images in website ..."
    find ./public/images -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)
fi

if [[ ($1 == "") || ($1 == "show_library")]]
then
    # Find Base images
    echo "Find Base images in library ..."
    find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \)
fi

if [[ ($1 == "") || ($1 == "remove_base")]]
then
    # Remove all Base images from public folder
    echo "Removing Base images from public folder ..."
    find ./public/images -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec rm -f {} \;
fi

if [[ ($1 == "") || ($1 == "copy")]]
then
    # Copy all Base images from library to public folder
    echo "Copying Base images to public folder ..."
    find ./library/data -type f \( -iname \*42*.tif -o -iname \*42*.tiff \) -exec cp -fv {} ./public/images \;
fi