import socket
import threading
from datetime import datetime
#ip =socket.gethostbyname(socket.gethostname())
ip="192.168.31.176"
port=8000

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
print("server ip address is "+ip)
server.listen(10)
client_info=list()

cmd={
    0:"shutdown()"
    ,1:"quit()"
    ,2:"sticker()"    
    }
    

def shutdown():
    print("send quit() to all threads and close all the threads")
    
    
def broadcast():
    pass

def server_recv(client):
    global client_info
    while True:
        message=str(client_info[client][0].recv(1024), encoding='utf-8')
        message=client_info[client][1][0]+" "+str(datetime.now().strftime("%H:%M:%S"))+" : "+message
        client_info[client][0].sendall(message.encode())
        
        if(cmd[0] in message):
            shutdown()
        elif(cmd[1] in message):
            print("[system]"+client_info[client][1][0]+" quit")
            client_info[client][0].close()
            client_info
            break
        elif(cmd[2] in message):
            print("print sticker")
        else:
            print(message)

        


while True:
    client=len(client_info)
    client_info.append(server.accept())
    print("[system]",client_info[client][1][0],"is online")
    server_recv(client)
    
    