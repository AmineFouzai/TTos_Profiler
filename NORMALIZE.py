
import face_recognition
from PIL import  Image
import  os
import cv2
import numpy as np

DATA_SET='data_set'
for directory in os.listdir(DATA_SET):
    for image in os.listdir(f'{DATA_SET}/{directory}'):
        if image.endswith('.jpg'):
            print(f'{DATA_SET}/{directory}/{image}')
            pil_image = Image.open(f'{DATA_SET}/{directory}/{image}') 
            pil_image.resize((500,500),Image.ANTIALIAS).save(f'{DATA_SET}/{directory}/{image}')
            print('Normalized and saved')
        