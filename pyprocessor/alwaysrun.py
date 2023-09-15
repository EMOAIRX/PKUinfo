import time
import os
import socket

while True:
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # result = sock.connect_ex(('localhost', 9001))
    # if result == 0:
    #     print("Port 9001 is open, starting server...")
    os.system("python3 /home/info/PKUinfo/pyprocessor/server.py &")
    
    #     break
    # else:
    #     print("Port 9001 is not open, waiting...")
    time.sleep(300)
