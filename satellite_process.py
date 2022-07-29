from abc import ABCMeta, abstractmethod
from satellite_packet import ImagePacket
from time import time
import math
from satellite_camera import Camera

class Satellite_Processor():

    def __init__(self):
        self.camera = Camera()
        return


    def generate_image_packet(self):
        packet = ImagePacket(self.get_image())
        return  packet.serialize()
    
    def satellite_process(self):
        image_packet = self.generate_image_packet()
        image_size = len(image_packet).to_bytes(4, byteorder='big')
        return image_size, image_packet

    def get_image(self):
        return self.camera.get_image() 