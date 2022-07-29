import cv2
import time
import numpy

class Camera():
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        # cv2.namedWindow('test')
    def get_image(self):
        
        ret, frame = self.capture.read()
        if ret == True :
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('test',frame)
            image_bytes = cv2.imencode('.bmp', frame)[1].tobytes()
            
            return image_bytes
        else :
            return b'\x00'