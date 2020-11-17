# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:13:02 2020

@author: asus
"""
import cv2

videoCapture = cv2.VideoCapture('Gary.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutPutVid.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
    fps,size)

success, frame = videoCapture.read()
#(success)


while success: #LOOP UNTIL THERE ARE NO MORE FRAMES
    videoWriter.write(frame)
    success, frame = videoCapture.read()


'''
cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutPutVid.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
    fps,size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1 #10 seconds of frames
while success and numFramesRemaining > 150:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
'''