import cv2
import numpy as np
I = cv2.imread('test.jpg')
I_blur = cv2.blur(I, (3,3))
cv2.imwrite('smooth_img.jpg', I_blur)