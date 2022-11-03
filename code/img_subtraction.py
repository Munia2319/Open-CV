# Python program to illustrate
# arithmetic operation of
# subtraction of pixels of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('G:\\Study\\STUDIES(JU CSE)\\BSC all sem\\study 4-2\\Machine learning\\Assignment\\ass_1\\Rest of the thing\\open_cv_code\\star-1.jpg')
image2 = cv2.imread('G:\\Study\\STUDIES(JU CSE)\\BSC all sem\\study 4-2\\Machine learning\\Assignment\\ass_1\\Rest of the thing\\open_cv_code\\dot.jpg')

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the subtracted image
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
