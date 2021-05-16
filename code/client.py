import socket
import threading
import eel

#ip =input("please input server ip address")
#ip="192.168.31.176"
#ip="127.0.1.1"
#port=8000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

eel.init("web")

def send():
    while(1):
        message=input("input:")
        client.sendall(message.encode())
        echo=str(client.recv(1024), encoding='utf-8')
        eel.show_story(echo+"\n")
        print(echo)
        if("quit()" in echo):
            break
    print("this thread ended")
    client.close()
    
@eel.expose
def connect(ip,port):
    port=int(port)
    global client
    client.connect((ip,port))
    send()



eel.start('main.html',size = (620,620))
