import socket
import time
from satellite_process import Satellite_Processor



class Satellite:
    def __init__(self):
        self.HOST = '192.168.2.115'
        self.PORT = 6060
        self.byte_size = 65535
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_data = 0
        self.processor = Satellite_Processor()
        print("Connecting To Sat GS Server")
        self.client_socket.connect((self.HOST, self.PORT))

    def protocol(self, cnt):
            
            sensor, image = self.processor.satellite_process()
            print("\nSensor Send {}".format(cnt))
            self.client_socket.send(sensor)
            print("\nImage Send {}".format(cnt+1))
            self.client_socket.send(image)
            
            time.sleep(1)
            return cnt + 2
            
       
       
        
        
        

if __name__ == "__main__":
    cnt = 0
    print("Initializing Satellite")
    satellite = Satellite()
    print("Start Satellite Protocol")
    while True : 
        try :
            cnt = satellite.protocol(cnt)
        except Exception as e:
            print(repr(e))
            break
    satellite.client_socket.close()
