#!/usr/bin/python

"""
    半双工聊天程序-服务器端
    消息发送出去后，要等到有回复了才能发送下一条消息
    服务启动后等待客户端消息，回复客户端消息。
"""

from socket import *
from time import ctime

HOST = ''
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    if data.decode('utf-8') =='bye':
        print('bye')
        break
    else:
        print(f"来自 {addr} 的消息：{data.decode('utf-8')}")
        print("...请回复：")
        my_msg = input('> ')
        udpSerSock.sendto(my_msg.encode('utf-8'), addr)
        print("消息已发送，等待对方回复..")

udpSerSock.close()
    

