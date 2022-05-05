# project name   : u & me chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2317))
server.listen()

print("Waiting for a client...")

client, clientAddress = server.accept()
print("Client Address  1 : ", clientAddress)
# print(f"Client Address 2 : {clientAddress}")

while True:
    ser_msg = client.recv(1024).decode('UTF-8')
    print(clientAddress, ":", ser_msg)

    # manual input data ------------------------------------------
    # ser_msg = b"Hi Client"
    # client.send(ser_msg)

    # shutdown server --------------------------------------------
    if ser_msg == 'bye':
        break

    # user input data ---------------------------------------------
    ser_msg = input("enter message for client : ").encode('UTF-8')
    client.send(ser_msg)
