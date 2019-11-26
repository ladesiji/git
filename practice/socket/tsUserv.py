#!/usr/bin/pyhton
# -*-coding=utf-8-*-

"""
    创建一个UDP服务器
    接收用户消息，加一下时间戳后消息返回
"""

import socket
from time import ctime

HOST = ""
PORT = 8421
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(f'{ctime()}  '.encode('utf-8') + data,addr)
    print(f"...received form and returned to:{addr}")

updSerSock.close()
