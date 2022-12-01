from imports import *

#================================================================
#
# Function: showImage(title, image)
#
# Description: This function is just a wrapper for the open cv
#              show image procedure since it has to be able to 
#              catch any opencv exceptions, and exception handling
#              in main makes it cluttered and hard to read.
#
# Returns: image | openCV image
#
#================================================================
def showImage(title, image, leave):

    try:
        cv2.imshow(title, image)
        cv2.waitKey(0)
        if not leave:
            cv2.destroyAllWindows()
    except Exception:
        print("Displaying image failed, perhaps the title was invalid or the image was corrupted. Exiting.")
        sys.exit(-1)

    return