# project name   : u & me chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 2317
client.connect((host, port))

print('\033[1m' + 'you connected to server...!' + '\033[0m')

while True:
    # manual input data ------------------------------------------
    # cl_msg = "Hello Server 👋"
    # client.send(cl_msg.encode('UTF-8'))

    # user input data --------------------------------------------
    cl_msg = input("Enter message for server : ")
    client.send(cl_msg.encode('UTF-8'))

    # shutdown server --------------------------------------------
    if cl_msg == 'bye':
        break

    cl_msg = client.recv(1024)
    print("Server : ", cl_msg.decode('UTF-8'))
