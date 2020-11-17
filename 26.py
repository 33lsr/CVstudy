# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 07:56:15 2020

@author: asus
"""

import numpy 
import cv2
'''
img = numpy.zeros((3,3),dtype=numpy.uint8)

img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img[0][0][0]=255
img[0][0][2]=255

cv2.imwrite('generatedImage.png',img)
'''

#G+R=yellow
#B+G=sky
#B+R=rose

#cv2.imwrite('MyGrayCat.png',grayImage)
#print(grayImage.shape)
#print(img.shape)

#for i in range(0,29):
#    for n in range(0,29):
#        grayImage[i][n]=0
#    i=i+1
#n=n+1
    
#grayImage[0][0]=0
img = cv2.imread('cat.jpg')
a = img[100:200,100:200]
size = a.shape
print(size)


cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()