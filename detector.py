import cv2
from PIL import Image
import os 
import numpy as np
import  face_recognition

USER_DIR='target'

Recognizer=cv2.face.LBPHFaceRecognizer_create()
Recognizer.read('data.yml')


unkown_face=face=face_recognition.load_image_file('{}/input.jpg'.format(USER_DIR))
unkown_face=cv2.cvtColor(unkown_face,cv2.COLOR_BGR2GRAY)

print(unkown_face)

_id,conf=Recognizer.predict(unkown_face)
if conf>=45 and conf <=80:
        print(conf)
        print(_id)
        print(True)
else:
        print(conf)
        print(_id)
        print(False)
        

