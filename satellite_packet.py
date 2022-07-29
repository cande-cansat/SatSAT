import struct


class ImagePacket():
    # def __init__(self):
    #     self.image = []         # 307200 bytes

    def __init__(self, image):
        self.image = image            # 307200 bytes

    def print_packet(self):
        print("image size : {}".format(len(self.image)))
    
    def serialize(self):
        return self.image
        