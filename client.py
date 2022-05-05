# project name   : u & me chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2317))

print("you connected to server...!")

cl_msg = "Hello Server 👋"
client.send(cl_msg.encode('UTF-8'))