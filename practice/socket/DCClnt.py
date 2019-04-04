#!/usr/bin/python

"""
    创建UDP客户端
    提示用户输入发送给服务器的消息
    并接收服务器返回的消息
"""

import socket
from time import sleep

HOST = '192.168.43.1'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.setblocking(0)

while True:
    try:
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    except Exception:
        sleep(1)
        pass
    else:
        if data.decode == 'bye':
            print("服务器挂断对话")
            break
        print(f"{ADDR[0]}> {data.decode('utf-8')}")
    sendmsg = input("> ")
    if sendmsg:
        udpCliSock.sendto(sendmsg.encode('utf-8'), ADDR)
    if sendmsg == 'bye':
        print("主动挂断对话")
        break

udpCliSock.close()
