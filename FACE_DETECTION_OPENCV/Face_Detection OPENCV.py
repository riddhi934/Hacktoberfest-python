import cv2
import sys
facecascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
videocapture = cv2.VideoCapture(0)
img_counter = 0

while True:
    # Capture by Frame 
    ret , frame = videocapture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)
    faces = facecascade.detectMultiScale(gray,
                                        scaleFactor = 1.5,
                                        minNeighbors = 5,
                                        minSize = (30,30),
                                        flags = cv2.CASCADE_SCALE_IMAGE)
    #Drawing rectangle around face :
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.circle(frame,(100,150),100,(100,100,0),2)
    #Display the resulting frame :
    cv2.imshow('FaceDetection',frame)
    
    if k % 256 == 27 : #escape key 
        break
    elif k%256 == 32: # space key
        img_name = "web_ka_pehla{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        img_counter += 1

videocapture.release()
cv2.destroyAllWindows()