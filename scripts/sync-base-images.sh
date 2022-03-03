#!/bin/bash

# Find and copy Base images from data folder to public folder.
# If a parameter is passed, it will execute only the specified step. Else, all of them
# will be executed sequentially.

# TODO: use a domain app to extract the list of Base images. Remove magic numbers.

# Show current Base images
if [[ ($1 == "") || ($1 == "show_website")]]
then
    echo "Current Base images in website ..."
    find ./public/images -type f \( -iname '*-52.*.jpg' -o -iname '*-52.*.jpeg' \)
fi

# Find Base images
if [[ ($1 == "") || ($1 == "show_library")]]
then
    echo "Find Base images in library ..."
    find ./library/data -type f \( -iname '*-52.*.tif' -o -iname '-52.*.tiff' \)
fi

# Remove all Base images from public folder
if [[ ($1 == "") || ($1 == "remove_base")]]
then
    echo "Removing Base images from public folder ..."
    find ./public/images -type f \( -iname '*-52.*.tif' -o -iname '*-52.*.tiff' \) -exec rm -f {} \;
fi

# Copy all Base images from library to public folder
if [[ ($1 == "") || ($1 == "copy")]]
then
    echo "Copying Base images to public folder ..."
    find ./library/data -type f \( -iname '*-52.*.tif' -o -iname '*-52.*.tiff' \) -exec cp -fv {} ./public/images \;
fi