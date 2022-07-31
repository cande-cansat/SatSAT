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
            # cv2.imshow('test',frame)
            image_bytes = cv2.imencode('.jpeg', frame)[1].tobytes()
            
            return image_bytes
        else :
            return b'\x00'