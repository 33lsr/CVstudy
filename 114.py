# -*- coding: utf-8 -*-

import cv2

face_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_eye.xml')

camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, 1.1, 1, minSize=(100, 100))
        if len(faces) == 2:
            (x1,y1,w1,h1) = faces[0]
            (x2,y2,w2,h2) = faces[1]
            face1 = frame[y1:y1+h1,x1:x1+w1]
            #shape1 = face1.shape
            face2 = frame[y2:y2+h2,x2:x2+w2]
            #shape2 = face2.shape
            #roi_face2 = cv2.resize(face2,(shape1[0],shape1[1]))
            #roi_face1 = cv2.resize(face1,(shape2[0],shape2[1]))
            #shaper1 = roi_face1.shape
            #shaper2 = roi_face2.shape
            frame[y1:y1+h2,x1:x1+w2] = face2
            frame[y2:y2+h1,x2:x2+w1] = face1
        else:
            pass
            
        '''
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(
                roi_gray, 1.1, 8, minSize=(40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x+ex, y+ey),
                              (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        '''
        cv2.imshow('Face Detection', frame)




        
'''
videoCapture = cv2.VideoCapture('biepaile.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'faceofbiepaile.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
    fps,size)

success, frame = videoCapture.read()
while success:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 1.3, 2, minSize=(120, 120))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(
            roi_gray, 1.1, 6, minSize=(40, 40))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x+ex, y+ey),
                          (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
    videoWriter.write(frame)
    success, frame = videoCapture.read()
'''