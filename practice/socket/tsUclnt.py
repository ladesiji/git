#!/usr/bin/python

"""
    创建UDP客户端
    提示用户输入发送给服务器的消息
    并接收服务器返回的消息
"""

import socket

HOST = '192.168.43.1'
PORT = 8421
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
