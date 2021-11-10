## Image resizing GitHub action

Resizes all the TIF images found under the "images_path" input parameter to fit the specified bounding rectangle. The resized images overwrites the original ones.

The action looks for .TIF, .TIFF, .tif and .tiff extensions under the specified folder, unrecursively.

Build docker image:
```
docker build -t image-resize .
```

Run docker image:
```
docker run  -e INPUT_IMAGES_PATH='/images' -e INPUT_WIDTH=2048 -e INPUT_HEIGHT=2048 image-resize  
```

### Usage

You need to add the action in your workflow:

```yaml
    - name: Resize synched imaged
    uses: ./.github/actions/resize-image
    with:
        images_path: public/images
        width: 512
        height: 512
```

### Outputs

This action doesn't generate any output.

### Development

The image resizing process uses the temporary folder of the host environment (/tmp) to save the image while it is
being transformed. Once the transformation finished, it copies it to the destination folder. The temporary image
is not deleted, a garbage collection or repo image disposal is assumed.

### Improvements

The transformation will always be applied regardless of the source image size.

A suggested improvement would be that it only is applied if the source image size is BIGGER than the target size, to
avoid upsamplings and/or unnecessary operations.
