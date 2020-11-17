# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:53:02 2020

@author: asus
"""

import cv2
#import numpy as np

"""
img = cv2.imread('cat.jpg')
cv2.imshow('my image',img)
cv2.waitKey()
cv2.destroyAllWindows()
"""

clicked = False
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_RBUTTONUP:
        clicked = True
        
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow',onMouse)

print('Showing camera feed. Click window or press any key to stop')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow',frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()