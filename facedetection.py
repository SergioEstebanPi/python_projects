# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml

import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

def detect():
    cap = cv2.VideoCapture(0)
    
    while True:
        _,img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x,y,w,h) in face:
            cv2.rectangule(img, (x,y), (x+w, y+h), (0,255,0), 2)
        
        cv2.imshow("Face detection", img)
        
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    
detect()