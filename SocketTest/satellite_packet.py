import struct

from yaml import serialize

class GpsPacket():
    def __init__(self, latitude, longitude, altitude):
        self.latitude = struct.pack('f',latitude)            # 4 bytes
        self.longitude = struct.pack('f',longitude)          # 4 bytes
        self.altitude = struct.pack('f',altitude)            # 4 bytes

    def serialize(self):
        serialized = bytearray()
        serialized += self.latitude
        serialized += self.longitude
        serialized += self.altitude
        return serialized

class SensorPacket():
    # def __init__(self):
    #     self.data_type = 0      # 1 byte
    #     self.latitude = 0       # 4 bytes
    #     self.longitude = 0      # 4 bytes
    #     self.altitude = 0       # 4 bytes
    #     self.heading = 0        # 4 bytes
    #     self.pitch = 0          # 4 bytes
    #     self.roll = 0           # 4 bytes
    #     self.yaw = 0            # 4 bytes
    #     self.x_acc = 0          # 4 bytes
    #     self.y_acc = 0          # 4 bytes
    #     self.z_acc = 0          # 4 bytes
    #     self.temperature = 0    # 4 bytes
    #     self.humidity = 0       # 4 bytes
    #     self.image = []         # 307200 bytes

    def __init__(self, data_type, latitude, longitude, altitude, heading, pitch, roll, yaw, x_acc, y_acc, z_acc, temperature, humidity):
        self.data_type = data_type          # 1 byte
        self.latitude = struct.pack('f',latitude)            # 4 bytes
        self.longitude = struct.pack('f',longitude)          # 4 bytes
        self.altitude = struct.pack('f',altitude)            # 4 bytes
        self.heading = struct.pack('f',heading)              # 4 bytes
        self.pitch = struct.pack('f',pitch)                  # 4 bytes
        self.roll = struct.pack('f',roll)                    # 4 bytes
        self.yaw = struct.pack('f',yaw)                      # 4 bytes
        self.x_acc = struct.pack('f',x_acc)                  # 4 bytes
        self.y_acc = struct.pack('f',y_acc)                  # 4 bytes
        self.z_acc = struct.pack('f',z_acc)                  # 4 bytes
        self.temperature = struct.pack('f',temperature)      # 4 bytes
        self.humidity = struct.pack('f',humidity)            # 4 bytes

    def print_packet(self):
        print("data_type : {}".format(self.data_type))
        print("latitude : {}".format(self.latitude))
        print("longitude : {}".format(self.longitude))
        print("altitude : {}".format(self.altitude))
        print("heading : {}".format(self.heading))
        print("pitch : {}".format(self.pitch))
        print("roll : {}".format(self.roll))
        print("yaw : {}".format(self.yaw))
        print("x_acc : {}".format(self.x_acc))
        print("y_acc : {}".format(self.y_acc))
        print("z_acc : {}".format(self.z_acc))
        print("temperature : {}".format(self.temperature))
        print("humidity : {}".format(self.humidity))

    def serialize(self):
        serialized = self.data_type
        serialized += self.latitude
        serialized += self.longitude
        serialized += self.altitude
        serialized += self.heading
        serialized += self.pitch
        serialized += self.roll
        serialized += self.yaw
        serialized += self.x_acc
        serialized += self.y_acc
        serialized += self.z_acc
        serialized += self.temperature
        serialized += self.humidity
        return serialized

class ImagePacket():
    # def __init__(self):
    #     self.data_type = 0      # 1 byte
    #     self.image = []         # 307200 bytes

    def __init__(self, data_type, image):
        self.data_type = data_type          # 1 byte
        self.image = image            # 4 bytes

    def print_packet(self):
        print("data_type : {}".format(self.data_type))
        print("image size : {}".format(len(self.image)))
        

    def serialize(self):
        serialized = self.data_type
        serialized += self.image
        return serialized
