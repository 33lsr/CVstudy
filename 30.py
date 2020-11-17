# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:49:07 2020

@author: asus
"""

import cv2
import numpy
import os

#make an array od 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

#Convert the array to make a 400*300 grayscale image
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

#Convert the array to make a 400*100 color image
bgrImage = flatNumpyArray.reshape(100,400,3)
bgrImage[:,:,1]=0
cv2.imwrite('RandomColor.png',bgrImage)

cat = cv2.imread('cat.jpg')
cat = cat/2
cv2.imwrite('catroi.jpg',cat)

print(cat.shape)
print(cat.size)
print(cat.dtype)

