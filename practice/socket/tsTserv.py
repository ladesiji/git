#!/usr/bin/python

import socket
from time import ctime

HOST = "192.168.43.1"
PORT = 8421
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print(f"...connected from:{addr}")

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        tcpCliSock.send(f'{ctime()} {data}'.encode('utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
