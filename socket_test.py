import socket
import time
import io
from satellite_process import Satellite_Processor



class Satellite:
    def __init__(self):
        self.HOST = '14.6.207.102'
        self.PORT = 6060
        self.byte_size = 65535
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_data = 0
        self.processor = Satellite_Processor()
        print("Connecting To Sat GS Server")
        self.client_socket.connect((self.HOST, self.PORT))

    def protocol(self, cnt):
            cnt = cnt + 1
            file_size, image = self.processor.satellite_process()
            
            print("\nImage Send {}".format(cnt))
            while True:
                self.client_socket.send(file_size)
                self.client_socket.sendall(image)
                self.client_socket.settimeout(5.0)
                ack = self.client_socket.recv(1)
                if len(ack)>0:
                    print("Got Response from SatGS : {}".format(ack))
                    break
                else :
                    print("Got no response from SatGS... Retry to send image {}".format(cnt))
            
            # time.sleep(0.16)
            return cnt
            
       
       
        
        
        

if __name__ == "__main__":
    while True:
        try:
            cnt = 0
            print("Initializing Satellite")
            satellite = Satellite()
            print("Start Satellite Protocol")
            while True : 
                try :
                    cnt = satellite.protocol(cnt)
                except Exception as e:
                    print(repr(e))
                    satellite.client_socket.close()
                    break
        except Exception as e:
            print(repr(e))
    