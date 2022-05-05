# project name   : u & me chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2317))

print("you connected to server...!")

# manual input data ------------------------------------------
# cl_msg = "Hello Server 👋"
# client.send(cl_msg.encode('UTF-8'))

# user input data --------------------------------------------
cl_msg = input("enter message for server : ")
client.send(cl_msg.encode('UTF-8'))

cl_msg = client.recv(1024)
print("Server : ", cl_msg.decode('UTF-8'))


