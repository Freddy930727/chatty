import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip="192.168.31.219"
port=8000
server.bind((ip,port))
print("server ip address is "+ip)
server.listen(10)
conn,temp=server.accept()
message=str(conn.recv(1024), encoding='utf-8')
print(message)