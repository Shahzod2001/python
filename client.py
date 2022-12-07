import socket

while True:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('192.168.137.52', 8089))
    message = input('Please enter your message: ')
    clientsocket.send(message.encode())