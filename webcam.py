# pip3 install opencv-python
import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("text.jpg", frame)
    result = False
    print('Image captured')
    
imgcapture.release()