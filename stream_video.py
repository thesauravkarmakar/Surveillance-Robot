from threading import Thread
import cv2 as cv
import numpy as np

class WebCamVideoStream:
    def _init_(self,src=0):
        self.stream = cv.VideoCapture(src)
        (self.grabbed,self.frame) = self.stream.read()

        self.stopped = False

    def start(self):
        Thread(target = self.update,args = ()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (self.grabbed,self.frame) = self.stream.read()

        def read(self):
            while True:
                if self.stopped:
                    return
                
                (self.grabbed,self.frame) = self.stream.read()

        def read(self):
            return self.frame

        def stop(self):
            self.stopped = True

        
cam = WebCamVideoStream(src=0).start()

while(1):
    frame = cam.read()
    cv.imshow('frame',frame)

    key = cv.waitKey(1)

    if key == 27:
        break

cv.destroyAllWindows()
cam.stop()
