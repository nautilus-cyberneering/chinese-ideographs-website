import os
import os.path
import glob

from resizing.resize import resize_image


def get_files_paths(input_path):
    files = glob.glob(input_path+'/*.tif') + glob.glob(input_path+'/*.TIF') + \
        glob.glob(input_path+'/*.tiff') + glob.glob(input_path+'/*.TIFF')
    return files


def parse_size_parametres():
    width = int(os.environ["INPUT_WIDTH"])
    height = int(os.environ["INPUT_HEIGHT"])
    return (width, height)


def main():

    def process_file(filename):
        print("Resizing ", filename, "to", output_size[0],
              "x", output_size[1])
        resize_image(filename, output_size)

    files_paths = get_files_paths(
        os.environ["INPUT_IMAGES_PATH"])
    output_size = parse_size_parametres()
    for image_path in files_paths:
        process_file(image_path)


if __name__ == "__main__":
    main()
