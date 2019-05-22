# this file is meant to read the video from a USB webcam
import numpy as np
import cv2
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('172.18.0.2',1883,60)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    # gray here is the gray frame you will be getting from a camera
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    if len(faces) > 0:
        rc,jpg = cv2.imencode('.png',frame)
        msg = jpg.tobytes()
        client.publish('image_msg',payload=msg)
       #  cv2.imwrite('./image.png',frame)

