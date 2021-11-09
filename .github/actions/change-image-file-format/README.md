## Image file format change GitHub action

Loads an image and saves it in the especified format, creating (if needed) the folder.

The format is automatically inferred by the PyVips (wrapper of LibVips) library, based on the extension especified in the "format" parameter.


Build docker image:
```
docker build -t change-image-format .
```

Run docker image:
```
docker run -e INPUT_IMAGES_PATH='/images' -e INPUT_FORMAT="jpg" change-image-format  
```

### Usage

You need to add the action in your workflow:

```yaml
    - name: Change file format of synched images
    uses: ./.github/actions/change-image-file-format
    with:
        images_path: public/images
        format: jpg
```

### Outputs

This action doesn't generate any output.

### Development

The action directly creates and writes the destination file after opening and reading the source file, with no 
temporary intermediate image. This implies that, if the destination format is the same as the source format, the
action may fail, because of the way the Libvips handles image processing (as a pipeline).

An image quality parameter of 95 is hardcoded in the transformation. This will be used for lossy formats like JPEG.

Current file formats supported by Libvips (that should be also supported by PyVips) are JPEG, JPEG2000, JPEG-XL, TIFF, PNG, WebP, HEIC, AVIF, FITS, Matlab, OpenEXR, PDF, SVG, HDR, PPM / PGM / PFM, CSV, GIF, Analyze, NIfTI, DeepZoom, and OpenSlide.

### Improvements

The action could check if the destination format is the same as the source format, and do nothing in that case.

The quality parameter used in the pyVips operation could be un-hardcoded and put as explicit parameter.