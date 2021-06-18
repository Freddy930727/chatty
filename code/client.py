import socket
import eel
import time
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

eel.init("web")


def recv():
    print("in recv()")
    while(1):
        echo=str(client.recv(1024), encoding='utf-8')
        eel.show_story(echo+"\n")
        if("quit()" in echo):
            break

@eel.expose
def send(msg):
    print("test1")
    if(len(msg)==0):
        eel.show_story("input is blank"+"\n")
    else:
        client.sendall(msg.encode())

@eel.expose
def connection(ip,port):
    global client
    port=int(port)
    client.connect((ip,port))
    recv_thread=threading.Thread(target=recv)
    recv_thread.start()
    recv_thread.join() 
     
    print("io thread both ended") 
    client.close() 
    eel.quit()




eel.start('main.html',size = (620,620),port=1024)
