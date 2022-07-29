from abc import ABCMeta, abstractmethod
from satellite_packet import GpsPacket, SensorPacket, ImagePacket
from time import time
import math
from satellite_camera import Camera

class Satellite_Processor():

    def __init__(self):
        self.camera = Camera()
        return
    
    def generate_sensor_packet(self):
        t = time()
        latitude, longitude, altitude = self.get_gps_data(t)
        heading, pitch, roll, yaw, x_acc, y_acc, z_acc = self.get_ten_axis_data(t)
        temperature, humidity = self.get_temp_hum_data(t)
        packet = SensorPacket(
            b'\x00',
            latitude, longitude, altitude,
            heading, pitch, roll, yaw, x_acc, y_acc, z_acc,
            temperature, humidity
        )
        return packet.serialize()

    def generate_gps_packet(self, cnt):
        time = 30
        gps_x = 0
        gps_y = 0
        gps_z = -300/((time/2)*(time/2))*cnt*(cnt-time)
        if gps_z <= 0 :
            gps_z = 0
        sat_pos = GpsPacket(
            gps_x, gps_y, gps_z
        )
        if cnt > time/2:
            tar_pos = GpsPacket(gps_x +10, gps_y + 10, gps_z +10)
        else :
            tar_pos = GpsPacket(-1, -1, -1)
        return sat_pos.serialize() + tar_pos.serialize()


    def generate_image_packet(self):
        t = time()
        packet = ImagePacket(
            b'\x01',
            self.get_image(t)
        )
        return packet.serialize()
    
    def satellite_process(self, cnt):
        sensor_packet = self.generate_sensor_packet()
        image_packet = self.generate_image_packet()
        gps_packet = self.generate_gps_packet(cnt)
        return sensor_packet, image_packet, gps_packet

    def get_gps_data(self,t):
        latitude = math.sin(t)
        longitude = math.cos(t)
        altitude = math.sin(t)
        return latitude, longitude, altitude

    def get_ten_axis_data(self, t):
        heading = math.sin(t)
        pitch = math.cos(t)
        roll = math.sin(t)
        yaw = math.sin(t)
        x_acc = math.cos(t)
        y_acc = math.sin(t)
        z_acc = math.cos(t)
        return heading, pitch, roll, yaw, x_acc, y_acc, z_acc
    
    def get_temp_hum_data(self, t):
        temperature = math.sin(t)
        humidity = math.cos(t)
        return temperature, humidity

    def get_image(self, t):
        img = self.camera.get_image(t)
        return img 