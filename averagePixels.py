from imports import *

#================================================================
#
# Function: averagePixels(image, depth)
#
# Description: This function scales the input image down
#              by averaging the pixels.
#
# Returns: resizedImg | type: openCV image 
#    OR
# Returns: image | original image unchanged
#
#================================================================
def averagePixels(image, depth):

    #loop over this method as many times as necessary to reach
    #the desired depth
    workingImg = image

    #check that depth supplied is not 0 (no alteration)
    if depth != 0:

        #execute as many times as needed
        for i in range(depth):

            #check for color
            if(len(workingImg.shape) == 2):

                #get image size each time
                rows, columns = workingImg.shape

                #image to hold the scaled down image
                downScaledImg = np.zeros(shape=(math.floor(rows/2), math.floor(columns/2), 3), dtype=np.uint8)

                #check to see if we are going beyond a scale of '1' in either direction since we are using floor
                if downScaledImg.shape[0] == 0 or downScaledImg.shape[1] == 0:
                    return workingImg

                #take the average of the 4 surrounding pixels and make 1 pixel
                for i in range(math.floor(rows/2)):
                        for j in range(math.floor(columns/2)):
                            downScaledImg[i,j] = int(.25 * (int(workingImg[2*i,2*j]) + int(workingImg[2*i,2*j+1]) + int(workingImg[2*i+1,2*j]) + int(workingImg[2*i+1,2*j+1])))

                #update the old workingImg to newly scaled image
                workingImg = downScaledImg

            else:

                #get image size each time
                rows, columns, pixel = workingImg.shape

                #image to hold the scaled down image
                downScaledImg = np.zeros(shape=(math.floor(rows/2), math.floor(columns/2), 3), dtype=np.uint8)

                #check to see if we are going beyond a scale of '1' in either direction since we are using floor
                if downScaledImg.shape[0] == 0 or downScaledImg.shape[1] == 0:
                    return workingImg

                #take the average of the 4 surrounding pixels and make 1 pixel
                for i in range(math.floor(rows/2)):
                        for j in range(math.floor(columns/2)):
                            for k in range(pixel):
                                downScaledImg[i,j, k] = int(.25 * (int(workingImg[2*i,2*j, k]) + int(workingImg[2*i,2*j+1, k]) + int(workingImg[2*i+1,2*j, k]) + int(workingImg[2*i+1,2*j+1, k])))

                #update the old workingImg to newly scaled image
                workingImg = downScaledImg

        #return manipulated image
        return workingImg

    #else, image fit, exit
    else:
        return image