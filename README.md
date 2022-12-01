# Image-Sampling-and-Quantization
This project took images and downscaled them, then upscaled them through duplication and averaging, and then compared the results visually

## Notes
This project built on the tkinter image browser class. It introduced the simple concepts of pixel averaging/removing alternating rows/columns from the image to downsample an image, and pixel duplication/interpolation to upsample an image. It allows the user to select the methods for upsampling and downsampling, and samples an input image at various 'depths' to show how each method effects the data contained within the image. 

## Usage:
<pre>
python sample.py -h -g -s sampling_method -d depth -i intensity -f imagefile
        -s : sampling method. 1 for pixel deletion/replication, 2 for pixel averaging/interpolation [default: 1]
        -d : Number of levels for downsampling [default: 1]
        -i : Intensity levels, between 1 and 7 [default: 1]  
        -f : Image input path
        -g : grayscale the input image [default: false]
