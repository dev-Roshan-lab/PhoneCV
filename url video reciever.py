import cv2
import numpy

url = 'http://192.XXX.XX.X:8080/video'
cap = cv2.VideoCapture(url)
face = cv2.CascadeClassifier('cascade.xml')
while(True):
    ret, frame = cap.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=50,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces :
            cv2.rectangle(frame,(x,y),(x+w, x+h),(255,0,0),2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            print(x)
        cv2.imshow('frame',frame)
        
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
