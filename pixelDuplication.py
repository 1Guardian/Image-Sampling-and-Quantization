from imports import *

#================================================================
#
# Function: pixelDuplication(image, depth)
#
# Description: This function scales the input image up
#              by duplication the odd rows and columns from the
#              image. It repeats this as many times as the input
#              variable 'depth' specifies it should.
#
# Returns: combinedImg | type: openCV image 
#    OR
# Returns: image | original image unchanged
#
#================================================================
def pixelDuplication(image, depth):

    #loop over this method as many times as necessary to reach
    #the desired depth
    resizedImg = image

    #check that depth supplied is not 0 (no alteration)
    if depth != 0:

        #execute as many times as needed
        for i in range(depth):

            #get size
            rows = resizedImg.shape[0]
            columns = resizedImg.shape[1]

            upScaledImg = np.zeros(shape=(math.ceil(rows*2), math.ceil(columns*2), 3), dtype=np.uint8)

            #duplicate each pixel in source image
            #into 4 pixels in destination
            for i in range(rows):
                for j in range(columns):
                    upScaledImg[2*i, 2*j] = resizedImg[i,j]
                    upScaledImg[2*i+1, 2*j] = resizedImg[i,j]
                    upScaledImg[2*i, 2*j+1] = resizedImg[i,j]
                    upScaledImg[2*i+1, 2*j+1] = resizedImg[i,j]

            #update the carry image
            resizedImg = upScaledImg

        #return manipulated image
        return resizedImg

    #else, image fit, exit
    else:
        return image