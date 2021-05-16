import socket

#ip =input("please input server ip address")
#ip="192.168.31.174"
ip="127.0.1.1"
port=8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

while(1):
    message=input("input:")
    
    client.sendall(message.encode())
    if(message=="quit()"):
    	break
client.close()
