import socket

serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('192.168.137.194',8089))
serversocket.listen(5) #become a server socket, maximum 5 connections

while True:
    connection, adress=serversocket.accept()
    buf=connection.recv(64)
    if len(buf)>0:
        print(buf)
    #break