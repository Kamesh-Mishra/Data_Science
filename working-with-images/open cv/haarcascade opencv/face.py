# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:21:42 2020

@author: USER
"""


# https://www.youtube.com/watch?v=2gIuopr6k5w&list=PLlUZLZydkS78ehCoOGF-b4aAgthf6Fz1D&index=2


import numpy
import cv2


face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


image = cv2.imread('index.jpg',0)

cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# our classifier returns the ROI of the detected face as a tuple
#it stores the top left coordinate and the bottom right coordinate

faces = face_casecade.detectMultiScale(image)

print(faces)

#when no faces detected, face_casecade returns and empty tuple
if faces is ():
    print("No faces found")
    
    
#we iterate through our faces array and draw a rectangle
# over each face in faces

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w-50,y+h-50), (100,0,0), 2)
    cv2.imshow('modi_face', image)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()



















