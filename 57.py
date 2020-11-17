# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:01:34 2020

@author: asus
"""

import cv2
import numpy
from scipy import ndimage

img = cv2.imread('lsr.jpg',0)
'''
kernel_3x3 = numpy.array([[-4,-2,0],
                       [-2,2,2],
                       [0,2,4]])
 
kernel_5x5 = numpy.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,4,2,-1],
                       [-1,1,2,1,-1],
                       [-1,-1,-1,-1,-1]])

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img,(17,17),0)
g_hpf = img - blurred
cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("blurred",blurred)
cv2.imshow("g_hpf",g_hpf)
'''

cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("canny.jpg"))


cv2.waitKey()
cv2.destroyAllWindows()