import cv2
from PIL import Image
import os 
import numpy as np
import  face_recognition
import  time
from halo import Halo

loader=Halo(text='Training Recognizer',color='blue',spinner='dots')
DATA_SET='data_set'
Reacognizer=cv2.face.LBPHFaceRecognizer_create() 
# Reacognizer=cv2.face.EigenFaceRecognizer_create() dosent work

ids=0
user_data=list()
labels=list()
for directory in os.listdir(DATA_SET):
    for image in os.listdir(f'{DATA_SET}/{directory}'):
        if image.endswith('.jpg'):
            print(f'{DATA_SET}/{directory}/{image}')
            data=face_recognition.load_image_file(f'{DATA_SET}/{directory}/{image}')
            gray=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
            user_data.append(gray)
            labels.append(ids)
    ids=ids+1

loader.start()
Reacognizer.train(np.array(user_data),np.array(labels))
Reacognizer.save('data.yml')
loader.stop()
