import os
import json
import glob

from change_image_file_format.change_image_file_format import change_image_file_format


def get_files_paths(input_path):
    files = glob.glob(input_path+'/*.tif') + glob.glob(input_path+'/*.TIF') + \
        glob.glob(input_path+'/*.tiff') + glob.glob(input_path+'/*.TIFF')
    return files


def get_output_filename(input_filename, format):
    splittedFilename = os.path.splitext(input_filename)
    return splittedFilename[0]+"."+format


def main():

    def process_file(filename):
        output_filename = get_output_filename(filename, format)
        print("Converting ", filename, "to", format,
              "as", output_filename)
        change_image_file_format(filename, output_filename)

    files_paths = get_files_paths(
        os.environ["INPUT_IMAGES_PATH"])
    format = os.environ["INPUT_FORMAT"]
    for image_path in files_paths:
        process_file(image_path)


if __name__ == "__main__":
    main()
