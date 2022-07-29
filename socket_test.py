import socket
import time
import io
from satellite_process import Satellite_Processor



class Satellite:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 6060
        self.byte_size = 65535
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_data = 0
        self.processor = Satellite_Processor()
        print("Connecting To Sat GS Server")
        self.client_socket.connect((self.HOST, self.PORT))

    def protocol(self, cnt):
            
            file_size, image = self.processor.satellite_process()
            
            print("\nImage Send {}".format(cnt+1))
            self.client_socket.send(file_size)
            self.client_socket.sendall(image)
            
            time.sleep(1)
            return cnt + 1
            
       
       
        
        
        

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
