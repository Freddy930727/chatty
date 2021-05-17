import socket
import threading
import eel
import time

#ip =input("please input server ip address")
#ip="192.168.31.176"
#ip="127.0.1.1"
#port=8000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

eel.init("web")

def send():
    while(1):
        message=input("input:")
        while(len(message)==0):
            message=input("input:")
        client.sendall(message.encode())
        if("quit()" in message):
            break
        

def recv():
    while(1):
        echo=str(client.recv(1024), encoding='utf-8')
        eel.show_story(echo+"\n")
        print(echo)
        if("quit()" in echo):
            break
    
    
        
@eel.expose
def connect(ip,port):
    global client
    port=int(port)
    client.connect((ip,port))
    
    send_thread=threading.Thread(target=send)
    recv_thread=threading.Thread(target=recv,)
    
    send_thread.start()
    recv_thread.start()
    
    
    send_thread.join()
    recv_thread.join()
    
    print("io thread both ended")
    client.close()
    eel.quit()
    



eel.start('main.html',size = (620,620))
