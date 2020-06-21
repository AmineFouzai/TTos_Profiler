from PIL import  Image
import  face_recognition
import cv2
import numpy as np
import os

USER_DIR='target'#change this to argument
USER_DIR_To_EXTRACT_FACE_FROM='user_images/skander_images'
DATA_SET='data_set'

#simple comparing faces function
def Simple_Faces_Compare(target_encoding,biometric_encoding):#SFC
        try:
            if(len(target_encoding)>0):target_encoding=target_encoding[0] 
            if(len(biometric_encoding)>0):biometric_encoding=biometric_encoding[0]
            return True if True in face_recognition.compare_faces([target_encoding],biometric_encoding) else False
        except Exception as e:
            print(e)
            None if len(target_encoding)>0 else print('No Face Found in target image')  
            None if len(biometric_encoding)>0 else print('No Face Found in the lookup image') 
            return None

#function that convertes RGB to GRAY FOR less SIZE and accurency
def RGB_TO_GARY(location,loaded_image,path):
    top,right,bottom,left=location[0]
    to_save=cv2.cvtColor(np.asarray(Image.fromarray(loaded_image[top:bottom,left:right])),cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{DATA_SET}/{path}',to_save)

#load image
user=face_recognition.load_image_file(f'{USER_DIR}/input.jpg')
user_face_location=face_recognition.face_locations(user)

#extract face save as GRAY image
RGB_TO_GARY(user_face_location,user,'input.jpg')

#encode image
user=face_recognition.face_encodings(user,user_face_location)

#walk dir to find images
for image in os.listdir(USER_DIR_To_EXTRACT_FACE_FROM):
        #load image
        face_or_faces=face_recognition.load_image_file(f'{USER_DIR_To_EXTRACT_FACE_FROM}/{image}')
        
        #extract face or faces
        locations=face_recognition.face_locations(face_or_faces)
        
        #walk face location
        for location in locations:
            
            #extract face by location
            face=face_recognition.face_encodings(face_or_faces,[location])
            #call comparing function and save
            if(Simple_Faces_Compare(user,face)):
                RGB_TO_GARY([location],face_or_faces,image)



