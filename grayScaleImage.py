from imports import *

#================================================================
#
# Function: saveJson(currentJson, newMetaData)
#
# Description: This function is just a wrapper for the open cv
#              grayscaling procedure since it has to be able to 
#              catch any opencv exceptions, and exception handling
#              in main makes it cluttered and hard to read.
#
# Returns: image | openCV image
#
#================================================================
def grayScaleImage(image):

    #add try catch protection to the openCV calls specifically
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception:
        print("Grayscaling provided image failed. Perhaps the image path was empty or invalid. Exiting.")
        sys.exit(-1)

    return image