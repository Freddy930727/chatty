import socket
import threading
#ip =socket.gethostbyname(socket.gethostname())
ip="192.168.31.176"
port=8000

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
print("server ip address is "+ip)
server.listen(10)
client_info=list()
info=[1,2]


    
    
    
def server_recv(client):
    global client_info
    message=str(client_info.recv(1024), encoding='utf-8')
    if(message !="quit()"):
        print(client_info[client][1][1]+' : '+message)
    else:
        print("[system]"+client_info[client][1][1]+" quit")
        client_info[client][0].close()


while True:
    client=len(client_info)
    
    info=server.accept()
    client_info.append(info)
    print(client_info[client][0])
    print()
    print(client_info[client][1])
    print("[system]",client_info[client][1][1],"is online")
    server_recv(client)
    
    