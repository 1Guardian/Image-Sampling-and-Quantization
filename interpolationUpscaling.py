from imports import *

#================================================================
#
# Function: interpolationUpscale(image, depth)
#
# Description: This function scales the input image up
#              by use of the interpolation function given
#              in the document
#
# Returns: resizedImg | type: openCV image 
#    OR
# Returns: image | original image unchanged
#
#================================================================
def interpolationUpscale(image, depth):

    #loop over this method as many times as necessary to reach
    #the desired depth
    workingImg = image

    #check that depth supplied is not 0 (no alteration)
    if depth != 0:

        #check if we have a color or grayscale image
        if(len(workingImg.shape) == 2):

            #execute as many times as needed
            for i in range(depth):

                #get image size each time
                rows, columns = workingImg.shape

                #image to hold the scaled up image
                upScaledImg = np.zeros(shape=(math.floor(rows*2), math.floor(columns*2), 3), dtype=np.uint8)

                #dimensions for new image
                new_dimensions = [math.floor(columns*2), math.floor(rows*2)]

                #loop over all old pixels (grayscale)
                for i in range(rows):
                    for j in range(columns):

                        print(j)

                         #get the first new pixel
                        upScaledImg[2*i, 2*j] = workingImg[i,j]

                         #get the second new pixel
                        if (i + 1 < rows):
                            upScaledImg[(2*i)+1, 2*j] = int(.5 * (workingImg[i,j] + workingImg[i+1,j]))
                        else:
                            upScaledImg[(2*i)+1, 2*j] = int(.5 * (workingImg[i,j] + workingImg[i,j]))

                         #get the third new pixel
                        if (j + 1 < columns):
                            upScaledImg[2*i, (2*j)+1] = int(.5 * (workingImg[i,j] + workingImg[i,j+1]))
                        else:
                            upScaledImg[2*i, (2*j)+1] = int(.5 * (workingImg[i,j] + workingImg[i,j]))

                        #get the fourth new pixel    
                        if (j + 1 < columns and i + 1 < rows):
                            upScaledImg[(2*i)+1, (2*j)+1] = int(.25 * (workingImg[i,j] + workingImg[i,j+1] + workingImg[i+1,j] + workingImg[i+1,j+1]))
                        else:
                            upScaledImg[(2*i)+1, (2*j)+1] = int(.25 * (workingImg[i,j] + workingImg[i,j] + workingImg[i,j] + workingImg[i,j]))

                #update the old workingImg to newly scaled image
                workingImg = upScaledImg

            #return manipulated image
            return workingImg
        
        else:
            #execute as many times as needed
            for i in range(depth):

                #get image size each time
                rows, columns, alpha = workingImg.shape

                #image to hold the scaled up image
                upScaledImg = np.zeros(shape=(math.ceil(rows*2), math.ceil(columns*2), 3), dtype=np.uint8)

                #dimensions for new image
                new_dimensions = [math.ceil(columns*2), math.ceil(rows*2)]

                #loop over all old pixels (color)
                for i in range(rows):
                    for j in range(columns):
                        
                        #get the first new pixel
                        for k in range(alpha):
                            upScaledImg[2*i, 2*j, k] = workingImg[i,j, k]

                        #get the second new pixel
                        for k in range(alpha):
                            if (i + 1 < rows):
                                upScaledImg[(2*i)+1, 2*j, k] = int(.5 * (int(workingImg[i,j, k]) + int(workingImg[i+1,j, k])))
                            else:
                                upScaledImg[(2*i)+1, 2*j, k] = int(.5 * (int(workingImg[i,j, k]) + int(workingImg[i,j, k])))

                        #get the third new pixel
                        for k in range(alpha):
                            if (j + 1 < columns):
                                upScaledImg[2*i, (2*j)+1, k] = int(.5 * (int(workingImg[i,j, k]) + int(workingImg[i,j+1, k])))
                            else:
                                upScaledImg[2*i, (2*j)+1, k] = int(.5 * (int(workingImg[i,j, k]) + int(workingImg[i,j, k])))
                        
                        #get the fourth new pixel 
                        for k in range(alpha):
                            if (j + 1 < columns and i + 1 < rows):
                                upScaledImg[(2*i)+1, (2*j)+1, k] = int(.25 * (int(workingImg[i,j, k]) + int(workingImg[i,j+1, k]) + int(workingImg[i+1,j, k]) + int(workingImg[i+1,j+1, k])))
                            else:
                                upScaledImg[(2*i)+1, (2*j)+1, k] = int(.25 * (int(workingImg[i,j, k]) + int(workingImg[i,j, k]) + int(workingImg[i,j, k]) + int(workingImg[i,j, k])))

                #update the old workingImg to newly scaled image
                workingImg = upScaledImg

            #return manipulated image
            return workingImg

    #else, image fit, exit
    else:
        return image