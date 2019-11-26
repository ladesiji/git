#!/usr/bin/python

from socket import *

HOST = "192.168.43.1"
PORT = 8421
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("> ")
    if not data:
        break
    tcpCliSock.send(f'{data}\r\n'.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode().strip())
    tcpCliSock.close()
