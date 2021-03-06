import numpy as np
import cv2

class catfacedetect():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.flag = True
        
    def detect(self, JobID):   
        #faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalcatface.xml')
        faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
        #cap = cv2.VideoCapture(0)
        self.cap.set(3,640) # set Width
        self.cap.set(4,480) # set Height

        while True:
            if not self.flag:
                return
            ret, img = self.cap.read()
            #img = cv2.flip(img, -1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale(
                gray,     
                scaleFactor=1.2,
                minNeighbors=5,     
                minSize=(20, 20)
            )
            
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]  
            
            cv2.imshow('video',img)
            #print(type(faces))
            
            k = cv2.waitKey(30)
            if len(faces) != 0:
                cv2.imwrite('opencv'+str(JobID)+'.png', img)
                break
            
        #self.cap.release()
        #cv2.destroyAllWindows()
        return
    
    def KillProcess(self):
        #cap = cv2.VideoCapture(0)
        self.flag = False
        self.cap.release()
        cv2.destroyAllWindows()
        return

if __name__ == '__main__':
    test = catfacedetect()
    test.detect(0)
    test.KillProcess()
