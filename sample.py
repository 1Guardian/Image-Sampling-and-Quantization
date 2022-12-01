#==============================================================================
#
# Class : CS 5420
#
# Author : Tyler Martin
#
# Project Name : Project 3 | Scaling Images
#
# Date: Oct 11 2022
#
# Description: This project works with downscaling and upscaling input images. 
#              The main purpose of the project is to learn how to scale images 
#              either by deletion or insertion of pixels determined by an 
#              arbitrary selection of even columns or even rows, and how to scale
#              images by averaging the pixels to scale them up or down. It also
#              works with intensity scaling as a final measure. 
#
# Notes: Since I know you prefer to read and work in C++, this file is set
#        up to mimic a standard C/C++ flow style, including a __main__()
#        declaration for ease of viewing. Also, while semi-colons are not 
#        required in python, they can be placed at the end of lines anyway, 
#        usually to denote a specific thing. In my case, they denote globals, 
#        and global access, just to once again make it easier to parse my code
#        and see what it is doing and accessing.
#
#==============================================================================

#"header" file imports
from imports import *
from checkImages import *
from averagePixels import *
from intensitySampling import *
from pixelDeletion import *
from pixelDuplication import *
from interpolationUpscaling import *
from showImage import *
from grayScaleImage import *

#================================================================
#
# NOTES: THE OUTPATH WILL HAVE THE LAST / REMOVED IF IT EXISTS
#        THE imageType WILL HAVE A . APPLIED TO THE FRONT AFTER
#        CHECKING VALIDITY
#
#================================================================


#================================================================
#
# Function: __main__
#
# Description: This function is the python equivalent to a main
#              function in C/C++ (added just for ease of your
#              reading, it has no practical purpose)
#
#================================================================

def __main__(argv):

    #variables that contain the command line switch
    #information
    inPath = "nothing"
    depth = 1
    mode = -1
    intensity = -1
    grayscale = -1
    leave = False

    # get arguments and parse
    try:
      opts, args = getopt.getopt(argv,"h:gls:d:i:f:")

    except getopt.GetoptError:
        print("sample.py -h -g -s sampling_method -d depth -i intensity -f imagefile")
        print("===========================================================================================================")
        print("-s : sampling method. 1 for pixel deletion/replication, 2 for pixel averaging/interpolation [default: 1]")
        print("-d : Number of levels for downsampling [default: 1]")
        print("-i : Intensity levels, between 1 and 7 [default: 1]")  
        print("-f : Image input path")  
        print("-g : grayscale the input image [defulat: false]")  
        sys.exit(2)

    for opt, arg in opts:

        if opt == ("-h"):
            print("sample.py -h -g -s sampling_method -d depth -i intensity -f imagefile")
            print("===========================================================================================================")
            print("-s : sampling method. 1 for pixel deletion/replication, 2 for pixel averaging/interpolation [default: 1]")
            print("-d : Number of levels for downsampling [default: 1]")
            print("-i : Intensity levels, between 1 and 7 [default: 1]")  
            print("-f : Image input path")  
            print("-g : grayscale the input image [defulat: false]")  
            sys.exit(2)

        elif opt == ("-s"):
            if (int(arg) < 3 and int(arg) > 0):
                mode = int(arg)
            else:
                print("Invalid Mode Supplied. Only Values 1 and 2 Are Accepted.")
                sys.exit(-1)

        elif opt == ("-d"):
            if (int(arg) > 0):
                depth = int(arg)
            else:
                print("Invalid Depth Supplied. Depth Must Be Positive")
                sys.exit(-1)

        elif opt in ("-i"):
            if (int(arg) > 0 and int(arg) < 8):
                intensity = int(arg)
            else:
                print("Invalid Intensity Supplied. Intensity Must Be Between 1 and 7")
                sys.exit(-1)

        elif opt == ("-f"):
            inPath = arg

        elif opt == ("-g"):
            grayscale = 1

        elif opt == ("-l"):
            leave = True

    #make sure we got at the least, a path
    if (inPath == "nothing"):
        print("you must provide a file to start with!")
        sys.exit(2)

    #if we are to use grayscale, then use it
    originalImage = checkImages(inPath)
    if (grayscale == 1):
        originalImage = grayScaleImage(checkImages(inPath))


    #just intensity sampling requested
    if (mode == -1 and intensity != -1):
        
        #Apply intensity sampling
        intensitySampled = intensitySampling(originalImage, intensity)

        #open window to see image
        showImage("Image Intensity Sampled", intensitySampled, leave)

    #handle operations based on desired mode
    elif (mode == 1):

        for i in range(depth+1):

            #show original
            if i == 0:
                showImage("Original Image", originalImage, leave)

            else:
        
                #handle downscaling of image first
                scaledDown = pixelDeletion(originalImage, i)

                #check if the user wanted intensity sampling
                if (intensity != -1):
                    scaledDown = intensitySampling(scaledDown, intensity)

                #open window to see image
                showImage("Image Scaled Down | Depth: " + str(i), scaledDown, leave)

                #handle upscaling of image next
                scaledUp = pixelDuplication(scaledDown, i)

                #open window to see image
                showImage("Image Scaled Up | Depth: " + str(i), scaledUp, leave)

    else:

        for i in range(depth+1):
        
            #show original
            if i == 0:
                showImage("Original Image", originalImage, leave)

            else:

                #handle downscaling of image first
                scaledDown = averagePixels(originalImage, i)

                #check if the user wanted intensity sampling
                if (intensity != -1):
                    scaledDown = intensitySampling(scaledDown, intensity)

                #open window to see image
                showImage("Image Scaled Down | Depth: " + str(i), scaledDown, leave)

                #handle upscaling of image next
                scaledUp = interpolationUpscale(scaledDown, i)

                #open window to see image
                showImage("Image Scaled Up | Depth: " + str(i), scaledUp, leave)

#start main
argv = ""
__main__(sys.argv[1:])